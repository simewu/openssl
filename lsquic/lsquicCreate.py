import os 

dir = "/home/pi/openssl/lsquic"

algorithm = ["dilithium2","dilithium3","dilithium5","dilithium2_aes","dilithium3_aes","dilithium5_aes"] 

for i in range(len(algorithm)):
    myCmd = '/home/pi/openssl/apps/openssl req -x509 -new -newkey '+algorithm[i]+' -keyout /home/pi/openssl/lsquic/'+algorithm[i]+'key_CA.key -out /home/pi/openssl/'+algorithm[i]+'key_CA.pem -nodes -subj "/CN=oqstest CA" -days 365 -config /home/pi/openssl/apps/openssl.cnf'
    os.system(myCmd)
    myCmd = '/home/pi/openssl/apps/openssl genpkey -algorithm '+algorithm[i]+' -out /home/pi/openssl/lsquic/'+algorithm[i]+'key_srv.pem '
    os.system(myCmd)
    myCmd = '/home/pi/openssl/apps/openssl req -new -newkey '+algorithm[i]+' -keyout /home/pi/openssl/lsquic/'+algorithm[i]+'key_srv.pem -out /home/pi/openssl/lsquic'+algorithm[i]+'key_srv.csr -nodes -subj "/CN=oqstest server" -config /home/pi/openssl/apps/openssl.cnf'
    os.system(myCmd)
    myCmd = '/home/pi/openssl/apps/openssl x509 -req -in /home/pi/openssl/lsquic/'+algorithm[i]+'key_srv.csr -out /home/pi/openssl/lsquic/'+algorithm[i]+'key_crt.pem -CA /home/pi/openssl/lsquic/'+algorithm[i]+'key_CA.pem -CAkey /home/pi/openssl/lsquic/'+algorithm[i]+'key_CA.key -CAcreateserial -days 365'
    os.system(myCmd)