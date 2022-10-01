"""Encrdec

The Python script to encrypt and decryption PII data like passwords.

Requirement:
    pycryptodome

Documentation:
    https://pycryptodome.readthedocs.io/en/latest/

Author:
    Adnan Yoztyurk
"""

from Crypto.Cipher import AES


def encryption(file_path):
    original_pii = input('Please enter the pii: ')

    # 16 digit key (have to be the same with "decryption")
    key = b'1\tx2\x18B\x97\x9cVS\x02"l\xee\xa8z'

    # Encryption
    cipher = AES.new(key, AES.MODE_EAX)
    pii_ciphertext, pii_tag = cipher.encrypt_and_digest(str.encode(original_pii))
    pii_nonce = cipher.nonce

    # Write encrypted bytes
    file_out = open(file_path, "wb")
    [file_out.write(x) for x in (pii_nonce, pii_tag, pii_ciphertext)]
    file_out.close()


def decryption(file_path):
    # 16 digit key (have to be the same with "decryption")
    key = b'1\tx2\x18B\x97\x9cVS\x02"l\xee\xa8z'

    length = 16

    # Decryption
    file_in = open(file_path, "rb")
    encrypted = file_in.read()
    pii_nonce1, pii_tag1, pii_ciphertext1 = [encrypted[i:i + length] for i in
                                             range(0, len(encrypted), length)]

    cipher = AES.new(key, AES.MODE_EAX, pii_nonce1)
    pii_byte = cipher.decrypt_and_verify(pii_ciphertext1, pii_tag1)

    global decrypted_pii
    decrypted_pii = pii_byte.decode("utf-8")
    return decrypted_pii

# End of script
