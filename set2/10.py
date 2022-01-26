from Crypto.Cipher import AES
from aes import base64decode_from_file, decrypt_aes_cbc

key = b"YELLOW SUBMARINE"
ctFile = "10.txt"
ciphertext = base64decode_from_file(ctFile)

print(decrypt_aes_cbc(ciphertext, key, bytes(16)))