import os 

openssl_dir = os.path.expanduser('~/openssl')


myCmd = f'{openssl_dir}/apps/openssl req -x509 -new -newkey rainbowIclassic -keyout key_CA.key -out key_CA.pem -nodes -subj "/CN=oqstest CA" -days 365 -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl genpkey -algorithm rainbowIclassic -out key_srv.key'
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl req -new -key key_srv.key -out key_srv.csr -nodes -subj \'/CN=oqstest server\' -config {openssl_dir}/apps/openssl.cnf'
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl x509 -req -in key_srv.csr -out key_crt.pem -CA key_CA.pem -CAkey key_CA.key -CAcreateserial -days 365' 
os.system(myCmd)

myCmd = f'{openssl_dir}/apps/openssl verify -CAfile key_CA.pem key_crt.pem key_crt.pem'
os.system(myCmd)