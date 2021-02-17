import os 

myCmd = 'openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out private-key.pem'
os.system(myCmd)