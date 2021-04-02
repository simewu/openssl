#install liboqs
sudo apt install cmake gcc libtool libssl-dev make ninja-build git python3-pytest python3-pytest-xdist unzip xsltproc doxygen graphviz

cd $PWD
sudo rm -r openssl
sudo rm -r liboqs

git clone https://github.com/open-quantum-safe/liboqs.git
git clone https://github.com/prchander/openssl.git

OPENSSL_DIR=$PWD/openssl
cd liboqs
mkdir build && cd build
cmake -GNinja -DOQS_USE_OPENSSL=ON ..
#cmake -GNinja -DBUILD_SHARED_LIBS=ON .. # LibOQS errors
cmake -GNinja -DCMAKE_INSTALL_PREFIX=$OPENSSL_DIR/oqs ..
ninja
sudo ninja install 

#install openssl
cd $OPENSSL_DIR
./Configure no-shared linux-x86_64 -lm
sudo make -j