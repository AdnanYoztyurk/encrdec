# encrdec
The Python script encrypts and decrypts PII data like passwords.

# About me
I love automating Python jobs. Most of them include data pipeline building for analytics purposes. 

# Situation
My scripts include queries, especially for data pre-processing. I need to feed my Oracle username and password to the Python scripts, to query PII data from the database. The challenge is that these scripts are automated and scheduled. So I checked out a convenient way to feed the Python scripts with PII. As none of the solutions worked for me, I built the approach below and made it work for me.

# Approach
There are two main parts (functions) of the process, encryption and decryption. 

**Encryption**: First, enter the PII and let "pycryptodome" encrypt it using AES. Then, the job will save the encrypted value to the .bin file on the given path.

**Decryption**: When the PII is encrypted, you address the .bin file path. Finally, decrypt the password in the script and run your script securely.

# Encryption

Use the following code to encrypt your PII data. 

import encrdec

file_path = r"C:\Github\file.bin" # Please change the file paths.

encrdec.encryption(file_path)

# Decryption

Use the following code to decrypt your PII data. 

import encrdec

file_path = r"C:\Github\file.bin" # Please address the file path you used for encryption.

encrdec.decryption(file_path)

# Author
Adnan Yoztyurk
