# ransomware

It's a simple version, to understand how ransomware works. 

Our ransomware is implemented in the file encrypter.py. It encrypts all files in the same directory and shows a ransom message, requesting financial amount of10 bitcoins for user to obtain the key. There is a safeguard, so in order to start the encryption the user have to enter "start".
To decrypt the file user have to provide the correct secret phrase (in this example "coffee"), it decrypts those files, otherwise they would stay encrypted.
