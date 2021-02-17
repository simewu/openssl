#Instructions for setting up openssl and liboqs 
#----------------------------------------------
#Assumptions: Ubuntu 20.04
#------------
#Build lsquic & OQS OpenSSL library:
#-----------------------------

sudo apt install cmake gcc libtool libssl-dev make ninja-build git python3-pytest python3-pytest-xdist unzip xsltproc doxygen graphviz
cd ~
rm -rf openssl
rm -rf liboqs 

git clone https://github.com/open-quantum-safe/liboqs.git

git clone https://github.com/prchander/openssl.git

OPENSSL_DIR=$PWD/openssl
cd ~


cd liboqs
mkdir build && cd build
cmake -GNinja -DBUILD_SHARED_LIBS=ON ..
ninja
cmake -GNinja -DCMAKE_INSTALL_PREFIX=OPENSSL_DIR/oqs ..
ninja
sudo ninja install

cd ~
cd openssl
./Configure no-shared linux-x86_64 -lm
sudo make -j
