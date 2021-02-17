import os 

dir = "/home/pi/openssl/lsquic"

algorithm = ["dilithium2","dilithium3","dilithium5","dilithium2_aes","dilithium3_aes","dilithium5_aes"] 

for i in range(len(algorithm)):
    myCmd = '/home/pi/openssl/apps/openssl req -x509 -new -newkey'+ algorithm[i] +'-keyout /home/pi/openssl/lsquic/'+algorithm[i]+'/key_CA.key -out /home/pi/openssl/'+algorithm[i]+'/key_CA.pem -nodes -subj "/CN=oqstest CA" -days 365 -config /home/pi/openssl/apps/openssl.cnf'
    os.system(myCmd)
    myCmd = '/home/pi/openssl/apps/openssl genpkey -algorithm'+ algorithm[i] +'-out /home/pi/openssl/lsquic/'+algorithm[i]+'/key_srv.pem'
    os.system(myCmd)
    myCmd = '/home/pi/openssl/apps/openssl req -new -newkey'+ algorithm[i] +'-keyout /home/pi/openssl/lsquic/'+algorithm[i]+'/key_srv.pem -out /home/pi/openssl/lsquic'+algorithm[i]+'/key_srv.csr -nodes -subj "/CN=oqstest server" -config /home/pi/openssl/apps/openssl.cnf'
    os.system(myCmd)
    myCmd = '/home/pi/openssl/apps/openssl x509 -req -in /home/pi/openssl/lsquic/'+algorithm[i]+'/key_srv.csr -out /home/pi/openssl/lsquic/'+algorithm[i]+'/key_crt.pem -CA /home/pi/openssl/lsquic/'+algorithm[i]+'/key_CA.pem -CAkey /home/pi/openssl/lsquic/'+algorithm[i]+'/key_CA.key -CAcreateserial -days 365'
    os.system(myCmd)


#if algorithm == "rsa":
#    myCmd = '/home/pi/openssl/apps/openssl req -x509 -new -newkey rsa -keyout key_CA.key -out key_CA.pem -pkeyopt rsa_keygen_bits:2048 -nodes -subj "/CN=oqstest CA" -days 365 -config /home/pi/openssl/apps/openssl.cnf'
 #   os.system(myCmd)
  #  myCmd = '/home/pi/openssl/apps/openssl genpkey -algorithm rsa -out key_srv.pem -pkeyopt rsa_keygen_bits:2048'
   # os.system(myCmd)
    #myCmd = '/home/pi/openssl/apps/openssl req -new -newkey rsa -keyout key_srv.pem -out key_srv.csr -nodes -pkeyopt rsa_keygen_bits:2048 -subj "/CN=oqstest server" -config /home/pi/openssl/apps/openssl.cnf'
    #os.system(myCmd)
    #myCmd = '/home/pi/openssl/apps/openssl x509 -req -in key_srv.csr -out key_crt.pem -CA key_CA.pem -CAkey key_CA.key -CAcreateserial -days 365'
    #os.system(myCmd)

#if algorithm == "Dilithium2":
 #   myCmd = '/home/pi/openssl/apps/openssl req -x509 -new -newkey Dilithium2 -keyout key_CA.key -out key_CA.pem -nodes -subj "/CN=oqstest CA" -days 365 -config /home/pi/openssl/apps/openssl.cnf'
 #   os.system(myCmd)
 #   myCmd = '/home/pi/openssl/apps/openssl genpkey -algorithm Dilithium2 -out key_srv.pem'
 #   os.system(myCmd)
 #   myCmd = '/home/pi/openssl/apps/openssl req -new -newkey Dilithium2 -keyout key_srv.pem -out key_srv.csr -nodes -subj "/CN=oqstest server" -config /home/pi/openssl/apps/openssl.cnf'
 #   os.system(myCmd)
 #   myCmd = '/home/pi/openssl/apps/openssl x509 -req -in key_srv.csr -out key_crt.pem -CA key_CA.pem -CAkey key_CA.key -CAcreateserial -days 365'
 #   os.system(myCmd)

#if algorithm == "falcon512":
 #   myCmd = '/home/pi/openssl/apps/openssl req -x509 -new -newkey falcon512 -keyout key_CA.key -out key_CA.pem -nodes -subj "/CN=oqstest CA" -days 365 -config /home/pi/openssl/apps/openssl.cnf'
 #   os.system(myCmd)
 #   myCmd = '/home/pi/openssl/apps/openssl genpkey -algorithm falcon512 -out key_srv.pem'
 #   os.system(myCmd)
 #   myCmd = '/home/pi/openssl/apps/openssl req -new -newkey falcon512 -keyout key_srv.pem -out key_srv.csr -nodes -subj "/CN=oqstest server" -config /home/pi/openssl/apps/openssl.cnf'
 #   os.system(myCmd)
 #   myCmd = '/home/pi/openssl/apps/openssl x509 -req -in key_srv.csr -out key_crt.pem -CA key_CA.pem -CAkey key_CA.key -CAcreateserial -days 365'
 #S   os.system(myCmd)