#function to generate random aes key:

import secrets
from aes import *
from numpy import byte
from Crypto.Cipher import AES

def generate_key(keysize):
    key = secrets.token_bytes(keysize)
    return key

def encrypt_aes_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def encrypt_aes_cbc(plaintext,key,iv):
    cipher = AES.new(key, AES.MODE_CBC, iv = iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext



def encryption_oracle(plaintext):
    """
    input: plaintext as a byte object
    output: ecb or ebc encrypted ciphertext
            under a random key.
            random IVs for CBC
    """
    
    plaintext = bytearray(plaintext)
    #generate random key to encrypt under
    key = generate_key(keysize= 16) # genertae a 16 byte = 16*8 = 128 bit key
    
    # add 5-10 random bytes before and after the plaintext
    random_bytes1 = secrets.token_bytes(secrets.choice([5,6,7,8,9,10]))
    random_bytes2 = secrets.token_bytes(secrets.choice([5,6,7,8,9,10]))
    plaintext = random_bytes1 + plaintext + random_bytes2
    

    # now pad plaintext to block size
    plaintext = PKCS7_padding(plaintext, 16)
    print("non unique blocks in plaintext:")
    print(get_non_unique_blocks(plaintext,16))
    print("---------------------")

    #print non distinct blocks

    #now encrypt half the time under ecb and half under cbc
    res = secrets.randbelow(2)
    if res == 1:
        #encrypt under ecb
        ciphertext = encrypt_aes_ecb(plaintext, key)
        print("encryption oracle: ecb")
    else:
        #encrypt under cbc with random Ivs
        ciphertext = encrypt_aes_cbc(plaintext, key, secrets.token_bytes(16))
        print("encryption oracle: cbc")
    return ciphertext


# plaintext = secrets.token_bytes(16*20)

with open("set2/11.txt") as pt:
    plaintextt = bytes(pt.read(), 'utf-8')

# plaintextt = b'\xd8\x80a\x97@\xa8\xa1\x9bx@\xa8\xa3\x1c\x81\n=\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xe2\xdd\x05/kd\x1d\xbf\x9d\x11\xb04\x85B\xbbW\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x94u\xc9\xdf\xdb\xc1\xd4e\x97\x94\x9d\x9c~\x82\xbfZ\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x97\xa9>\xab\x8dj\xec\xd5fH\x91Tx\x9ak\x03\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xd4\x03\x18\x0c\x98\xc8\xf6\xdb\x1f*?\x9c@@\xde\xb0\xabQ\xb2\x993\xf2\xc1#\xc5\x83\x86\xb0o\xba\x18j'

key = generate_key(16)
cipher = encryption_oracle(plaintextt)
# print(len(cipher))


if  detect_ecb(cipher,16)== True:
    print("ECB mode: TRUE")
else:
    print("ECB mode: FALSE")

