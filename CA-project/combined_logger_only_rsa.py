# A separate file is saved for every individual algorithm, but samples themselves are overwritten

import os 
import time
import datetime

num_samples = int(input("Enter number of times to loop: \n"))

openssl_dir = os.path.expanduser('~/openssl')

def initCert(algorithm, bits = ''):
	if algorithm == 'rsa':
		#myCmd = f'{openssl_dir}/apps/openssl req -x509 -new -newkey rsa:{bits} -keyout key_CA_{algorithm}{bits}.key -out key_CA_{algorithm}{bits}.pem -pkeyopt rsa_keygen_bits:{bits} -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		myCmd = f'{openssl_dir}/apps/openssl req -x509 -new -newkey rsa:{bits} -keyout key_CA_{algorithm}{bits}.key -out key_CA_{algorithm}{bits}.pem -pkeyopt rsa_keygen_bits:{bits} -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		os.system(myCmd)
	if algorithm == 'secp':
		myCmd =f'{openssl_dir}/apps/openssl ecparam -out key_CA_{algorithm}{bits}.key -name {algorithm}{bits} -genkey > /dev/null 2>&1'
		os.system(myCmd)
		myCmd =f'{openssl_dir}/apps/openssl req -new -key key_CA_{algorithm}{bits}.key -x509 -nodes -days 365 -out key_CA_{algorithm}{bits}.pem -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		os.system(myCmd)
	else:
		myCmd = f'{openssl_dir}/apps/openssl req -x509 -new -newkey {algorithm} -keyout key_CA_{algorithm}{bits}.key -out key_CA_{algorithm}{bits}.pem -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		os.system(myCmd)

def genKey(algorithm, num_samples, bits = ''):
	if algorithm == 'rsa':
		#myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm rsa -out key_srv_{algorithm}{bits}.key -pkeyopt rsa_keygen_bits:{bits} > /dev/null 2>&1'
		myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm rsa -out key_srv_{algorithm}{bits}.key -pkeyopt rsa_keygen_bits:{bits} > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	if algorithm == 'secp':
		myCmd =f'{openssl_dir}/apps/openssl ecparam -out key_srv_{algorithm}{bits}.key -name secp{bits} -genkey > /dev/null 2>&1'
		for i in range(num_samples):
			os.system(myCmd)
	else:
		myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm {algorithm} -out key_srv_{algorithm}{bits}.key > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)

def genCSR(algorithm, num_samples, bits = ''):
	if algorithm == 'rsa':
		#myCmd = f'{openssl_dir}/apps/openssl req -new -key key_srv_{algorithm}{bits}.key -out key_srv_{algorithm}{bits}.csr -nodes -pkeyopt rsa_keygen_bits:{bits} -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		myCmd = f'{openssl_dir}/apps/openssl req -new -key key_srv_{algorithm}{bits}.key -out key_srv_{algorithm}{bits}.csr -nodes -pkeyopt rsa_keygen_bits:{bits} -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	if algorithm == 'secp':
		myCmd =f'{openssl_dir}/apps/openssl req -newkey ec:key_CA_{algorithm}{bits}.key -keyout ec_PRIVATEKEY.key -out key_srv_{algorithm}{bits}.csr -nodes -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	else:
		myCmd = f'{openssl_dir}/apps/openssl req -new -key key_srv_{algorithm}{bits}.key -out key_srv_{algorithm}{bits}.csr -nodes -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)

def genCert(algorithm, num_samples, bits =''):

	if algorithm == 'secp':
		myCmd=f'{openssl_dir}/apps/openssl x509 -req -in key_srv_{algorithm}{bits}.csr -out key_crt_{algorithm}{bits}.pem -CA key_CA_{algorithm}{bits}.pem -CAkey key_CA_{algorithm}{bits}.key -CAcreateserial -days 365 > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	else:
		#myCmd = f'{openssl_dir}/apps/openssl x509 -req -in key_srv_{algorithm}{bits}.csr -out key_crt_{algorithm}{bits}.pem -CA key_CA_{algorithm}{bits}.pem -CAkey key_CA_{algorithm}{bits}.key -CAcreateserial -days 365 > /dev/null 2>&1' 
		myCmd = f'{openssl_dir}/apps/openssl x509 -req -in key_srv_{algorithm}{bits}.csr -out key_crt_{algorithm}{bits}.pem -CA key_CA_{algorithm}{bits}.pem -CAkey key_CA_{algorithm}{bits}.key -CAcreateserial -days 365 > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)



def certVerify(algorithm, num_samples, bits = ''):
	if algorithm == 'secp':
		myCmd = f'{openssl_dir}/apps/openssl verify -CAfile key_CA_{algorithm}{bits}.pem key_crt_{algorithm}{bits}.pem key_crt_{algorithm}{bits}.pem > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	else:
		#myCmd = f'{openssl_dir}/apps/openssl verify -CAfile {openssl_dir}/CA-project/key_CA_{algorithm}{bits}.pem key_crt_{algorithm}{bits}.pem key_crt_{algorithm}{bits}.pem > /dev/null 2>&1'
		myCmd = f'{openssl_dir}/apps/openssl verify -CAfile {openssl_dir}/CA-project/key_CA_{algorithm}{bits}.pem key_crt_{algorithm}{bits}.pem key_crt_{algorithm}{bits}.pem > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)


algorithms = [
	'rsa'
]
algorithms_in_english = [
	'RSA'
]

def header():
	line = 'Timestamp,'
	line += 'Timestamp (Seconds),'
	line += 'Algorithm,'
	line += 'Algorithm (human readable),'
	line += 'Avg Key Gen Time (ms),'
	line += 'Avg Cert Signing Request Time (ms),'
	line += 'Avg Cert Gen Time (ms),'
	line += 'Avg Cert Verifying Time (ms),'
	return line

def run(file):
	rsa_bits_array = [2048, 3072, 4096];
	ecdsa_bits_array = ['256k1','384r1','521r1'];
	
	for i, algorithm in enumerate(algorithms):
		algorithm_in_english = algorithms_in_english[i]
		print(f'Starting {algorithm}...')
		time.sleep(0.1)

		if algorithm == 'rsa':
			for bits in rsa_bits_array:
				#print(f'Starting {algorithm} {bits}...')
				initCert(algorithm, bits)

				t1 = time.time()
				genKey(algorithm, num_samples, bits)
				t2 = time.time()
				avg_key_gen_time = (t2 - t1) / num_samples * 1000
				#print('Key generation time: ')
				#print(avg_key_gen_time)
				time.sleep(0.1)

				t1 = time.time()
				genCSR(algorithm, num_samples, bits)
				t2 = time.time()
				avg_cert_signing_request_time = (t2 - t1) / num_samples * 1000
				#print('CSR generation time')
				#print(avg_cert_signing_request_time)
				time.sleep(0.1)

				t1 = time.time()
				genCert(algorithm, num_samples, bits)
				t2 = time.time()
				avg_cert_gen_time = (t2 - t1) / num_samples * 1000
				#print('Certificate generation time')
				#print(avg_cert_gen_time)
				time.sleep(0.1)

				t1 = time.time()
				certVerify(algorithm, num_samples, bits)
				t2 = time.time()
				avg_cert_verify_time = (t2 - t1) / num_samples * 1000
				#print('Certificate verifying time')
				#print(avg_cert_verify_time)
				time.sleep(0.1)

				now = datetime.datetime.now()
				time_end = (now - datetime.datetime(1970, 1, 1)).total_seconds()
				line = f'{now},{time_end},{algorithm} {bits},{algorithm_in_english} {bits},{avg_key_gen_time},{avg_cert_signing_request_time},{avg_cert_gen_time},{avg_cert_verify_time},'
				file.write(line + '\n')

		elif algorithm == 'secp':
			for bits in ecdsa_bits_array:
				#print(f'Starting {algorithm} {bits}...')
				initCert(algorithm, bits)

				t1 = time.time()
				genKey(algorithm, num_samples, bits)
				t2 = time.time()
				avg_key_gen_time = (t2 - t1) / num_samples * 1000
				#print('Key generation time: ')
				#print(avg_key_gen_time)
				time.sleep(0.1)

				t1 = time.time()
				genCSR(algorithm, num_samples, bits)
				t2 = time.time()
				avg_cert_signing_request_time = (t2 - t1) / num_samples * 1000
				#print('CSR generation time')
				#print(avg_cert_signing_request_time)
				time.sleep(0.1)

				t1 = time.time()
				genCert(algorithm, num_samples, bits)
				t2 = time.time()
				avg_cert_gen_time = (t2 - t1) / num_samples * 1000
				#print('Certificate generation time')
				#print(avg_cert_gen_time)
				time.sleep(0.1)

				t1 = time.time()
				certVerify(algorithm, num_samples, bits)
				t2 = time.time()
				avg_cert_verify_time = (t2 - t1) / num_samples * 1000
				#print('Certificate verifying time')
				#print(avg_cert_verify_time)
				time.sleep(0.1)

				now = datetime.datetime.now()
				time_end = (now - datetime.datetime(1970, 1, 1)).total_seconds()
				line = f'{now},{time_end},{algorithm} {bits},{algorithm_in_english}{bits},{avg_key_gen_time},{avg_cert_signing_request_time},{avg_cert_gen_time},{avg_cert_verify_time},'
				file.write(line + '\n')

		else:
			#print(f'Starting {algorithm}...')
			initCert(algorithm)

			t1 = time.time()
			genKey(algorithm, num_samples)
			t2 = time.time()
			avg_key_gen_time = (t2 - t1) / num_samples * 1000
			#print('Key generation time: ')
			#print(avg_key_gen_time)
			time.sleep(0.1)

			t1 = time.time()
			genCSR(algorithm, num_samples)
			t2 = time.time()
			avg_cert_signing_request_time = (t2 - t1) / num_samples * 1000
			#print('CSR generation time: ')
			#print(avg_cert_signing_request_time)
			time.sleep(0.1)

			t1 = time.time()
			genCert(algorithm, num_samples)
			t2 = time.time()
			avg_cert_gen_time = (t2 - t1) / num_samples * 1000
			#print('Certificate generation time')
			#print(avg_cert_gen_time)
			time.sleep(0.1)

			t1 = time.time()
			certVerify(algorithm, num_samples)
			t2 = time.time()
			avg_cert_verify_time = (t2 - t1) / num_samples * 1000
			#print('Certificate verifying time')
			#print(avg_cert_verify_time)
			time.sleep(0.1)
			
			now = datetime.datetime.now()
			time_end = (now - datetime.datetime(1970, 1, 1)).total_seconds()
			line = f'{now},{time_end},{algorithm},{algorithm_in_english},{avg_key_gen_time},{avg_cert_signing_request_time},{avg_cert_gen_time},{avg_cert_verify_time},'
			file.write(line + '\n')




fileName = 'NEW_LOGGED_OPENSSL_FINAL1.csv'
file = open(fileName, 'w')
file.write(header() + '\n')
run(file)
