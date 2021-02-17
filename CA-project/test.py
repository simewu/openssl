import os

myCmd = '/home/pi/openssl/apps/openssl genpkey -algorithm rsa -out key_srvTest1.key -pkeyopt rsa_keygen_bits:4096'
os.system(myCmd)
myCmd = '/home/pi/openssl/apps/openssl req -new -key key_srvTest1.key -out key_srvTest1.csr -nodes -pkeyopt rsa_keygen_bits:4096 -subj "/CN=oqstest server" -config /home/pi/openssl/apps/openssl.cnf'
os.system(myCmd)