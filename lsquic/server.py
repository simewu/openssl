import os

myCmd = '/home/pi/openssl/apps/openssl s_server -cert key_crt.pem -key key_srv.pem -accept 44330 -www -tls1_3'
os.system(myCmd)