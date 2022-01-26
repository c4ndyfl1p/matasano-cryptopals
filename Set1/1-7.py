import base64

with open("Set1/7.txt") as ct:
    ciphertext = base64.b64decode(ct.read())

print(ciphertext)

with open("Set1/7dec.txt", "w") as file1:
    file1.write(str(ciphertext)[2:-1])

from Crypto.Cipher import AES

key = b'YELLOW SUBMARINE'

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
# print(plaintext)

# to convert the key to hex, and use it in openssl
key1 = [ord(i) for i in "YELLOW SUBMARINE"]
key2 = [hex(i)[2:] for i in key1]
key3 = "".join(key2)
print(key3)

#openssl enc -aes-128-ecb -d -a -in 7.txt -K "59454c4c4f57205355424d4152494e45"