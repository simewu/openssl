import os 

openssl_dir = os.path.expanduser('~/openssl')


myCmd = f'{openssl_dir}/apps/openssl req -x509 -new -newkey rsa:4096 -keyout key_CA_{4096}.key -out key_CA_{4096}.pem -pkeyopt rsa_keygen_bits:4096 -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm rsa -out key_srv_{4096}.key -pkeyopt rsa_keygen_bits:4096'
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl req -new -key key_srv_{4096}.key -out key_srv_{4096}.csr -nodes -pkeyopt rsa_keygen_bits:4096 -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl x509 -req -in key_srv_{4096}.csr -out key_crt_{4096}.pem -CA key_CA_{4096}.pem -CAkey key_CA_{4096}.key -CAcreateserial -days 365' 
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl verify -CAfile key_CA_{4096}.pem key_crt_{4096}.pem key_crt_{4096}.pem'
os.system(myCmd)