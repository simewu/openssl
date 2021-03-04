import os 

openssl_dir = os.path.expanduser('~/openssl')

#CA key
myCmd =f'{openssl_dir}/apps/openssl ecparam -out ec_CA_key.pem -name secp384r1 -genkey '
os.system(myCmd)
#CA cert
myCmd =f'{openssl_dir}/apps/openssl req -new -key ec_CA_key.pem -x509 -nodes -days 365 -out CA_cert.pem -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)
#server key
myCmd =f'{openssl_dir}/apps/openssl ecparam -out ec_key.pem -name secp384r1 -genkey'
os.system(myCmd)
#generating CSR
myCmd =f'{openssl_dir}/apps/openssl req -newkey ec:ec_CA_key.pem -keyout ec_PRIVATEKEY.key -out ec_csr.csr -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)
#CA signed certs
myCmd=f'{openssl_dir}/apps/openssl x509 -req -in ec_csr.csr -out ec_srv.crt -CA CA_cert.pem -CAkey ec_CA_key.pem -CAcreateserial -days 365'
os.system(myCmd)
#cert verify
myCmd = f'{openssl_dir}/apps/openssl verify -verbose -CAfile /home/pki/openssl/CA-project/ecdsa/ec_CA_key.pem /home/pki/openssl/CA-project/ecdsa/ec_srv.crt'
os.system(myCmd)
