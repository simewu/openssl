import os 

openssl_dir = os.path.expanduser('~/openssl')

#CA key
#myCmd =f'{openssl_dir}/apps/openssl ecparam -out key_CA.key -name secp521r1 -genkey '
#os.system(myCmd)
#CA cert
myCmd =f'{openssl_dir}/apps/openssl req -new -key key_CA.key -x509 -nodes -days 365 -out key_CA.pem -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)
#server key
myCmd =f'{openssl_dir}/apps/openssl ecparam -out key_srv.key -name secp521r1 -genkey'
os.system(myCmd)
#generating CSR
myCmd =f'{openssl_dir}/apps/openssl req -newkey ec:key_CA.key -keyout ec_PRIVATEKEY.key -out key_srv.csr -nodes -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)
#CA signed certs
myCmd=f'{openssl_dir}/apps/openssl x509 -req -in key_srv.csr -out key_crt.pem -CA key_CA.pem -CAkey key_CA.key -CAcreateserial -days 365'
os.system(myCmd)
#cert verify
myCmd = f'{openssl_dir}/apps/openssl verify -CAfile key_CA.pem key_crt.pem key_crt.pem'
os.system(myCmd)