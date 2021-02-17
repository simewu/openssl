import os 
import time

count = input("Enter number of times to loop: \n")
count = int(count)
alg = input("Enter alg to use: \n")


if alg == 'rsa':
    bits = input("Enter bits for rsa")
    myCmd = '/home/pi/openssl/apps/openssl req -x509 -new -newkey rsa -keyout key_CA.key -out key_CA.pem -pkeyopt rsa_keygen_bits:'+bits+' -nodes -subj "/CN=oqstest CA" -days 365 -config /home/pi/openssl/apps/openssl.cnf > /dev/null 2>&1'
    os.system(myCmd)

else:
    myCmd = '/home/pi/openssl/apps/openssl req -x509 -new -newkey '+alg+' -keyout key_CA.key -out key_CA.pem -nodes -subj "/CN=oqstest CA" -days 365 -config /home/pi/openssl/apps/openssl.cnf > /dev/null 2>&1'
    os.system(myCmd)

startTime = time.time() 

for i in range (count):
    current = i 
    current = str(current)

    myCmd = '/home/pi/openssl/apps/openssl x509 -req -in /home/pi/openssl/CA-project/csr/key_srv'+current+'.csr -out /home/pi/openssl/CA-project/crt/key_crt'+current+'.pem -CA key_CA.pem -CAkey key_CA.key -CAcreateserial -days 365'    
    os.system(myCmd)

endTime = time.time()

print ("Time taken:")
print (endTime-startTime)