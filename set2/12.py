import base64
from pprint import pprint
from django.urls import base
from aes import *

def aes_128_ecb_append(your_string, unkown_string, key):
    """
    input: yourstring as python byte object
    unkownstring: base 64 encoded
    key: 16 byte python byte object

    output: ciphertext
    """
    unkown_string = base64.b64decode(unkown_string)
    plaintext = your_string + unkown_string
    plaintext = PKCS7_padding(plaintext, 16)
    ciphertext = encrypt_aes_ecb(plaintext,key)
    return ciphertext

key = b'dTP\xdc"\xb8\xa4\x12\xe3H\xfc\xd5zS\x02\xf2'
unknown_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
print(len(base64.b64decode(unknown_string)))
res = aes_128_ecb_append(b"AAAAAAAAAAAAAAAR", unknown_string, key)
detect_ecb(res, 16)
print(len(res))
a = get_blocks_in_list(res,16)
pprint(a)
