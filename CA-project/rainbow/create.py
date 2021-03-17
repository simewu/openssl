import os 
import time 

openssl_dir = os.path.expanduser('~/openssl')

myCmd = f'{openssl_dir}/apps/openssl req -x509 -new -newkey rsa:3072 -keyout key_CA_{3072}.key -out key_CA_{3072}.pem -pkeyopt rsa_keygen_bits:3072 -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm rsa -out key_srv_{3072}.key -pkeyopt rsa_keygen_bits:3072'
startTime = time.time()
os.system(myCmd)
#endTime = time.time()
#print ("key gen time")
#print (endTime-startTime)

myCmd = f'{openssl_dir}/apps/openssl req -new -key key_srv_{3072}.key -out key_srv_{3072}.csr -nodes -pkeyopt rsa_keygen_bits:3072 -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf'
startTime = time.time()
os.system(myCmd)
#endTime = time.time()
#print ("csr gen")
#print (endTime-startTime)

myCmd = f'{openssl_dir}/apps/openssl x509 -req -in key_srv_{3072}.csr -out key_crt_{3072}.pem -CA key_CA_{3072}.pem -CAkey key_CA_{3072}.key -CAcreateserial -days 365' 
startTime = time.time()
os.system(myCmd)
#endTime = time.time()
#print ("cert gen time")
#print (endTime-startTime)


myCmd = f'{openssl_dir}/apps/openssl verify -CAfile key_CA_{3072}.pem key_crt_{3072}.pem key_crt_{3072}.pem'
startTime = time.time()
os.system(myCmd)
#endTime = time.time()
#print ("verify time")
#print (endTime-startTime)
