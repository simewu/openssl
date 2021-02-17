import os 
myCmd = 'echo "X" | apps/openssl s_client -connect 10.0.0.218:44330 -CAfile key_CA.pem > /dev/null 2>&1'
os.system(myCmd)