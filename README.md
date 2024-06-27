## Binutils
```
mkdir /tmp/src
cd /tmp/src

curl -O http://ftp.gnu.org/gnu/binutils/binutils-2.35.tar.gz
tar xf binutils-2.35.tar.gz

mkdir build-binutils
cd build-binutils

../binutils-2.35/configure --target=i686-elf --prefix=/usr/local/i686-elf --disable-nls --disable-werror

make
sudo make install
```

