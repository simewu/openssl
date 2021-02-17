import os 
import time 

count = input("Enter number of times to loop: \n")
count = int(count)
number = count
alg = input("Enter alg to use: \n")

if alg == "rsa":
    bits = input("enter bits for rsa")
    startTime = time.time()
    for i in range (count):
        current = i 
        current = str(current)

        myCmd = '/home/pi/openssl/apps/openssl genpkey -algorithm rsa -out /home/pi/openssl/CA-project/csr/key_srv'+current+'.key -pkeyopt rsa_keygen_bits:'+bits+' > /dev/null 2>&1'
        os.system(myCmd) 

    endTime = time.time()
    print ("Key generation time: ")
    print (endTime-startTime)

    startTime = time.time()
    for i in range (number):
        number = i 
        number = str(number)
        myCmd = '/home/pi/openssl/apps/openssl req -new -key /home/pi/openssl/CA-project/csr/key_srv'+number+'.key -out /home/pi/openssl/CA-project/csr/key_srv'+number+'.csr -nodes -pkeyopt rsa_keygen_bits:2048 -subj "/CN=oqstest server" -config /home/pi/openssl/apps/openssl.cnf > /dev/null 2>&1'
        os.system(myCmd)

    endTime = time.time()
    print ("csr generation time")
    print (endTime-startTime)

else:
    startTime = time.time()
    for i in range (count):
        current = i 
        current = str(current)

        myCmd = '/home/pi/openssl/apps/openssl genpkey -algorithm '+alg+' -out /home/pi/openssl/CA-project/csr/key_srv'+current+'.key > /dev/null 2>&1'
        os.system(myCmd)

    endTime = time.time()
    print ("Key generation time: ")
    print (endTime-startTime)

    startTime = time.time()
    for i in range (number):
        number = i 
        number = str(number)
        myCmd = '/home/pi/openssl/apps/openssl req -new -key /home/pi/openssl/CA-project/csr/key_srv'+number+'.key -out /home/pi/openssl/CA-project/csr/key_srv'+number+'.csr -nodes -subj "/CN=oqstest server" -config /home/pi/openssl/apps/openssl.cnf > /dev/null 2>&1'
        os.system(myCmd)

    endTime = time.time()
    print ("Csr generation time: ")
    print (endTime-startTime)