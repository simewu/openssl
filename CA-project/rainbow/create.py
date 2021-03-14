import os 

openssl_dir = os.path.expanduser('~/openssl')


myCmd = f'{openssl_dir}/apps/openssl req -x509 -new -newkey rsa:2048 -keyout key_CA_{2048}.key -out key_CA_{2048}.pem -pkeyopt rsa_keygen_bits:2048 -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm rsa -out key_srv_{2048}.key -pkeyopt rsa_keygen_bits:2048'
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl req -new -key key_srv_{2048}.key -out key_srv_{2048}.csr -nodes -pkeyopt rsa_keygen_bits:2048 -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl x509 -req -in key_srv_{2048}.csr -out key_crt_{2048}.pem -CA key_CA_{2048}.pem -CAkey key_CA_{2048}.key -CAcreateserial -days 365' 
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl verify -CAfile key_CA_{2048}.pem key_crt_{2048}.pem key_crt_{2048}.pem'
os.system(myCmd)