import base64
from pprint import pprint

from aes import *

# def aes_128_ecb_append(your_string, unkown_string, key):
#     """
#     Encruption oracle - appends your string to the unknown string and encrypts under ecb mode. Can be used as an encryption oracle.
    
#     input: "yourstring" as python byte object
#     unkownstring: base 64 encoded string. Function will decode it and then append it
#     key: 16 byte(128 bit) python byte object

#     output: ciphertext
#     """
#     #making the payload
    
#     plaintext = your_string + unkown_string

#     #actual encryption oracle
#     plaintext = PKCS7_padding(plaintext, 16)
#     ciphertext = encrypt_aes_ecb(plaintext,key)
#     return ciphertext

key = b'dTP\xdc"\xb8\xa4\x12\xe3H\xfc\xd5zS\x02\xf2'
unknown_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
# print(f"length of unknows string is {len(base64.b64decode(unknown_string))}")
# res = aes_128_ecb_append(b"", base64.b64decode(unknown_string), key) # how to use the oracle








# 1. Feed identical bytes of your-string to the function 1 at a time --- 
# start with 1 byte ("A"), then "AA", then "AAA" and so on. Discover the 
# block size of the cipher. You know it, but do this step anyway.
def detect_block_size(unknown_string):
    # should be independednt of chaineing mode or block cipher
    # steps:
    # 1. count the size of the ciphertext
    # 2. Keep adding A's in the beggining and querying the oracle until size changes. When size changes:
    # 3. the block size is the difference between the two sizes    
    
    
    original_size = len(aes_128_ecb_append(b"", base64.b64decode(unknown_string), key)) 
    print(f"original size of ciphertext: {original_size} bytes")

    # add A's and query oracle until size changes
    new_size = len(aes_128_ecb_append(b"", base64.b64decode(unknown_string), key))
    mystring = b'A'
    while (original_size==new_size):        
        new_size = len(aes_128_ecb_append(mystring, base64.b64decode(unknown_string), key))
        mystring = mystring + b'A'

    print(f"new size of ciphertext: {new_size} bytes")
    
    blocksize = new_size - original_size
    return blocksize

#==============================================================================
blocksize = detect_block_size(unknown_string) #1

# Detect that the function is using ECB. You already know, but do this step anyways.
res = aes_128_ecb_append(b"", base64.b64decode(unknown_string), key) #
if detect_ecb(res, 16) == True:
    print("detected ECB mode: TRUE")
else:
    print("detected ECB mode: FALSE")
print(len(res))

#3. Knowing the block size, craft an input block that is exactly 1 byte short 
# (for instance, if the block size is 8 bytes, make "AAAAAAA"). Think about 
# what the oracle function is going to put in that last byte position.
res = aes_128_ecb_append(b"AAAAAAAAAAAAAAAA", base64.b64decode(unknown_string), key) #input of 16 bytes
a = get_blocks_in_list(res,16)
pprint(a[0])

res = aes_128_ecb_append(b"AAAAAAAAAAAAAAA", base64.b64decode(unknown_string), key) #input of 16 bytes
a = get_blocks_in_list(res,16)
pprint(a[0])