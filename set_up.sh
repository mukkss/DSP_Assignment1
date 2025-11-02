#!/bin/bash

# Root folder
PROJECT_ROOT="DSAP_ASSIGNMENT1"

echo "Creating folder structure for $PROJECT_ROOT ..."

# Root
mkdir -p $PROJECT_ROOT
cd $PROJECT_ROOT || exit

# Root files
touch README.md .gitignore requirements.txt

### ASCII Encoder ###
mkdir -p ascii_encoder/{ascii_encoder,tests,logs,data}
touch ascii_encoder/README.md ascii_encoder/requirements.txt ascii_encoder/main.py
touch ascii_encoder/ascii_encoder/{__init__.py,encoder.py,decoder.py}
touch ascii_encoder/tests/test_ascii_encoder.py

### Caesar Cipher GUI ###
mkdir -p caesar_cipher_gui/{caesar_cipher_gui,tests,logs,data,assets/icons}
touch caesar_cipher_gui/README.md caesar_cipher_gui/requirements.txt caesar_cipher_gui/main.py
touch caesar_cipher_gui/caesar_cipher_gui/{__init__.py,cipher.py,gui.py}
touch caesar_cipher_gui/tests/test_caesar_cipher.py

### RSA Key Generation ###
mkdir -p rsa_key_generation/{rsa_key_generation,tests,logs,data,keys/private,keys/public}
touch rsa_key_generation/README.md rsa_key_generation/requirements.txt rsa_key_generation/main.py
touch rsa_key_generation/rsa_key_generation/{__init__.py,rsa_utils.py,crypto_ops.py}
touch rsa_key_generation/tests/test_rsa.py

echo "✅ Folder structure created successfully!"
