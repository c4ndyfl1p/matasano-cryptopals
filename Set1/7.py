from aes import decrypt_aes_ecb, base64decode_from_file

key = b"YELLOW SUBMARINE"    


ciphertext= base64decode_from_file("Set1/7.txt")
# print(ciphertext)

plaintext = decrypt_aes_ecb(ciphertext, key)
print(plaintext.decode('utf-8'))