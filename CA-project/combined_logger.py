import os 
import time
import datetime

num_samples = int(input("Enter number of times to loop: \n"))

openssl_dir = os.path.expanduser('~/openssl')

def initCert(algorithm, bits = ''):
	if algorithm == 'rsa':
		myCmd = f'{openssl_dir}/apps/openssl req -x509 -new -newkey rsa -keyout key_CA_{algorithm}{bits}.key -out key_CA_{algorithm}{bits}.pem -pkeyopt rsa_keygen_bits:{bits} -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		os.system(myCmd)
	else:
		myCmd = f'{openssl_dir}/apps/openssl req -x509 -new -newkey {algorithm} -keyout key_CA_{algorithm}{bits}.key -out key_CA_{algorithm}{bits}.pem -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		os.system(myCmd)

def genKey(algorithm, num_samples, bits = ''):
	if algorithm == 'rsa':
		myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm rsa -out {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.key -pkeyopt rsa_keygen_bits:{bits} > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	else:
		myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm {algorithm} -out {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.key > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)

def genCSR(algorithm, num_samples, bits = ''):
	if algorithm == 'rsa':
		myCmd = f'{openssl_dir}/apps/openssl req -new -key {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.key -out {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.csr -nodes -pkeyopt rsa_keygen_bits:{bits} -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	else:
		myCmd = f'{openssl_dir}/apps/openssl req -new -key {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.key -out {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.csr -nodes -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)

def genCert(algorithm, num_samples, bits =''):
	myCmd = f'{openssl_dir}/apps/openssl x509 -req -in {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.csr -out {openssl_dir}/CA-project/crt/key_crt_{algorithm}{bits}.pem -CA key_CA_{algorithm}{bits}.pem -CAkey key_CA_{algorithm}{bits}.key -CAcreateserial -days 365' 
	for i in range (num_samples):
		os.system(myCmd)

def certVerify(algorithm, num_samples, bits = ''):
	myCmd = f'{openssl_dir}/apps/openssl verify -CAfile {openssl_dir}/CA-project/key_CA_{algorithm}{bits}.pem {openssl_dir}/CA-project/crt/key_crt_{algorithm}{bits}.pem {openssl_dir}/CA-project/crt/key_crt_{algorithm}{bits}.pem'
	for i in range (num_samples):
		os.system(myCmd)



algorithms = ['rsa', 'dilithium2', 'dilithium3', 'dilithium5', 'dilithium2_aes', 'dilithium3_aes', 'dilithium5_aes' 'falcon512', 'falcon1024', 'rsa3072_dilithium2', 'rsa3072_dilithium3','rsa4096_dilithium5', 'rsa3072_falcon512','rsa4096_falcon512', 'p256_dilithium2', 'p256_dilithium3', 'p384_dilithium5', 'p256_falcon512','p384_falcon1024'] #, 'p512_falcon512']

def header():
	line = 'Timestamp,'
	line += 'Timestamp (Seconds),'
	line += 'Algorithm,'
	line += 'Avg Key Gen Time (s),'
	line += 'Avg Cert Signing Request Time (s),'
	line += 'Avg Cert Gen Time (s),'
	line += 'Avg Cert Verifying Time (s),'
	return line

def run(file):
	rsa_bits_array = [2048, 3072, 4096];
	
	for algorithm in algorithms:

		if algorithm == 'rsa':
			for bits in rsa_bits_array:
				print(f'Starting {algorithm} {bits}...')
				initCert(algorithm, bits)

				t1 = time.time()
				genKey(algorithm, num_samples, bits)
				t2 = time.time()
				avg_key_gen_time = (t2 - t1) / num_samples
				print('Key generation time: ')
				print(avg_key_gen_time)

				t1 = time.time()
				genCSR(algorithm, num_samples, bits)
				t2 = time.time()
				avg_cert_signing_request_time = (t2 - t1) / num_samples
				print('CSR generation time')
				print(avg_cert_signing_request_time)

				t1 = time.time()
				genCert(algorithm, num_samples, bits)
				t2 = time.time()
				avg_cert_gen_time = (t2 - t1) / num_samples
				print('Certificate generation time')
				print(avg_cert_gen_time)

				t1 = time.time()
				certVerify(algorithm, num_samples, bits)
				t2 = time.time()
				avg_cert_verify_time = (t2 - t1) / num_samples
				print('Certificate verifying time')
				print(avg_cert_verify_time)

				now = datetime.datetime.now()
				time_end = (now - datetime.datetime(1970, 1, 1)).total_seconds()
				line = f'{now},{time_end},{algorithm} {bits},{avg_key_gen_time},{avg_cert_signing_request_time},{avg_cert_gen_time},{avg_cert_verify_time},'
				file.write(line + '\n')


		else:
			print(f'Starting {algorithm}...')
			initCert(algorithm)

			t1 = time.time()
			genKey(algorithm, num_samples)
			t2 = time.time()
			avg_key_gen_time = (t2 - t1) / num_samples
			print('Key generation time: ')
			print(avg_key_gen_time)

			t1 = time.time()
			genCSR(algorithm, num_samples)
			t2 = time.time()
			avg_cert_signing_request_time = (t2 - t1) / num_samples
			print('CSR generation time: ')
			print(avg_cert_signing_request_time)

			t1 = time.time()
			genCert(algorithm, num_samples)
			t2 = time.time()
			avg_cert_gen_time = (t2 - t1) / num_samples
			print('Certificate generation time')
			print(avg_cert_gen_time)

			t1 = time.time()
			certVerify(algorithm, num_samples)
			t2 = time.time()
			avg_cert_verify_time = (t2 - t1) / num_samples
			print('Certificate verifying time')
			print(avg_cert_verify_time)
			
			now = datetime.datetime.now()
			time_end = (now - datetime.datetime(1970, 1, 1)).total_seconds()
			line = f'{now},{time_end},{algorithm},{avg_key_gen_time},{avg_cert_signing_request_time},{avg_cert_gen_time},{avg_cert_verify_time},'
			file.write(line + '\n')




fileName = 'NEW_LOGGED_OPENSSL.csv'
file = open(fileName, 'w')
file.write(header() + '\n')
run(file)
