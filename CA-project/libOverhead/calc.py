import os 
import time 

openssl_dir = os.path.expanduser('~/openssl')

myCmd = f'{openssl_dir}/apps/openssl req -x509 -new -newkey > /dev/null 2>&1'
startTime = time.time()
for i in range(1000):
    os.system(myCmd)
endTime = time.time()
print (f'Time for CA key and cert API {(endTime-startTime)/1000}')
myCmd = f'{openssl_dir}/apps/openssl genpkey > /dev/null 2>&1'
startTime = time.time()
for i in range(1000):
    os.system(myCmd)
endTime = time.time()
print (f'Time API for Server private key {(endTime-startTime)/1000}')
myCmd = f'apps/openssl req -new -key > /dev/null 2>&1'
startTime = time.time()
for i in range(1000):
    os.system(myCmd)
endTime = time.time()
print (f'Time API for CSR gen {(endTime-startTime)/1000}')
myCmd = f'apps/openssl x509 -req -in > /dev/null 2>&1'
startTime = time.time()
for i in range(1000):
    os.system(myCmd)
endTime = time.time()
print (f'Time API for cert gen {(endTime-startTime)/1000}')
myCmd = f'{openssl_dir}/apps/openssl verify -CAfile > /dev/null 2>&1'
startTime = time.time()
for i in range(1000):
    os.system(myCmd)
endTime = time.time()
print (f'Time for verify API {(endTime-startTime)/1000}')