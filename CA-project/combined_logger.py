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
		#myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm rsa -out {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.key -pkeyopt rsa_keygen_bits:{bits} > /dev/null 2>&1'
		myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm rsa -out {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.key -pkeyopt rsa_keygen_bits:{bits} > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	if algorithm == 'secp':
		myCmd =f'{openssl_dir}/apps/openssl ecparam -out key_srv_{algorithm}{bits}.key -name secp{bits} -genkey > /dev/null 2>&1'
		for i in range(num_samples):
			os.system(myCmd)
	else:
		myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm {algorithm} -out {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.key > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)

def genCSR(algorithm, num_samples, bits = ''):
	if algorithm == 'rsa':
		#myCmd = f'{openssl_dir}/apps/openssl req -new -key {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.key -out {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.csr -nodes -pkeyopt rsa_keygen_bits:{bits} -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		myCmd = f'{openssl_dir}/apps/openssl req -new -key {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.key -out {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.csr -nodes -pkeyopt rsa_keygen_bits:{bits} -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		for i in range (num_samples):	
			os.system(myCmd)
	if algorithm == 'secp':
		myCmd =f'{openssl_dir}/apps/openssl req -newkey ec:key_CA_{algorithm}{bits}.key -keyout ec_PRIVATEKEY.key -out key_srv_{algorithm}{bits}.csr -nodes -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	else:
		myCmd = f'{openssl_dir}/apps/openssl req -new -key {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.key -out {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.csr -nodes -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)

def genCert(algorithm, num_samples, bits =''):

	if algorithm == 'secp':
		myCmd=f'{openssl_dir}/apps/openssl x509 -req -in key_srv_{algorithm}{bits}.csr -out key_crt_{algorithm}{bits}.pem -CA key_CA_{algorithm}{bits}.pem -CAkey key_CA_{algorithm}{bits}.key -CAcreateserial -days 365 > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	else:
		#myCmd = f'{openssl_dir}/apps/openssl x509 -req -in {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.csr -out {openssl_dir}/CA-project/crt/key_crt_{algorithm}{bits}.pem -CA key_CA_{algorithm}{bits}.pem -CAkey key_CA_{algorithm}{bits}.key -CAcreateserial -days 365 > /dev/null 2>&1' 
		myCmd = f'{openssl_dir}/apps/openssl x509 -req -in {openssl_dir}/CA-project/csr/key_srv_{algorithm}{bits}.csr -out {openssl_dir}/CA-project/crt/key_crt_{algorithm}{bits}.pem -CA key_CA_{algorithm}{bits}.pem -CAkey key_CA_{algorithm}{bits}.key -CAcreateserial -days 365 > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)



def certVerify(algorithm, num_samples, bits = ''):
	if algorithm == 'secp':
		myCmd = f'{openssl_dir}/apps/openssl verify -CAfile key_CA_{algorithm}{bits}.pem key_crt_{algorithm}{bits}.pem key_crt_{algorithm}{bits}.pem > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)
	else:
		#myCmd = f'{openssl_dir}/apps/openssl verify -CAfile {openssl_dir}/CA-project/key_CA_{algorithm}{bits}.pem {openssl_dir}/CA-project/crt/key_crt_{algorithm}{bits}.pem {openssl_dir}/CA-project/crt/key_crt_{algorithm}{bits}.pem > /dev/null 2>&1'
		myCmd = f'{openssl_dir}/apps/openssl verify -CAfile {openssl_dir}/CA-project/key_CA_{algorithm}{bits}.pem {openssl_dir}/CA-project/crt/key_crt_{algorithm}{bits}.pem {openssl_dir}/CA-project/crt/key_crt_{algorithm}{bits}.pem > /dev/null 2>&1'
		for i in range (num_samples):
			os.system(myCmd)


algorithms = [
	'rsa', 'secp','dilithium2','dilithium3','dilithium5','dilithium2_aes','dilithium3_aes','dilithium5_aes',
	'falcon512', 'falcon1024', 'rainbowIclassic','rainbowIcircumzenithal','rainbowIcompressed',
	'rainbowIIIclassic','rainbowIIIcircumzenithal','rainbowIIIcompressed','rainbowVclassic','rainbowVcircumzenithal','rainbowVcompressed',
	'rsa3072_dilithium2','rsa3072_falcon512','rsa3072_rainbowIclassic','rsa3072_rainbowIcircumzenithal','rsa3072_rainbowIcompressed',
	'p256_dilithium2','p256_falcon512','p384_dilithium3', 'p521_dilithium5',
	'p521_falcon1024','p256_rainbowIclassic','p256_rainbowIcircumzenithal','p256_rainbowIcompressed',
	'p384_rainbowIIIclassic','p384_rainbowIIIcircumzenithal','p384_rainbowIIIcompressed','p521_rainbowVclassic','p521_rainbowVcircumzenithal','p521_rainbowVcompressed'
]
algorithms_in_english = [
	'RSA', 'P', 'Dilithium 2', 'Dilithium 3', 'Dilithium 5', 'Dilithium 2 with AES', 'Dilithium 3 with AES', 'Dilithium 5 with AES',
	'Falcon 512', 'Falcon 1024', 'Rainbow I Classic','Rainbow I Circumzenithal','Rainbow I Compressed',
	'Rainbow III Classic','Rainbow III Circumzenithal','Rainbow III Compressed','Rainbow V Classic','Rainbow V Circumzenithal','Rainbow V Compressed',
	'RSA 3072 + Dilithium 2','RSA 3072 + Falcon 512', 'RSA 3072 + Rainbow I Classic','RSA 3072 + Rainbow I Circumzenithal','RSA 3072 + Rainbow I Compressed',
	'P256 + Dilithium 2', 'P256 + Falcon 512','P384 + Dilithium 3', 'P521 + Dilithium 5',
	'P521 + Falcon 1024','P256 + Rainbow I Classic','P256 + Rainbow I Circumzenithal','P256 + Rainbow I Compressed',
	'P384 + Rainbow III Classic','P384 + Rainbow III Circumzenithal','P384 + Rainbow III Compressed','P521 + Rainbow V Classic','P521 + Rainbow V Circumzenithal','P521 + Rainbow V Compressed'
]

#algorithms = [
#	'rsa','rsa3072_rainbowIcompressed','rsa3072_dilithium2'
#]
#algorithms_in_english = [
#	'RSA','RSA 3072 + Rainbow I Compressed','RSA 3072 + Dilithium2'
#]

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
