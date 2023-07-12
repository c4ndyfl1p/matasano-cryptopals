
from Crypto.Cipher import AES
import base64, binascii, secrets

from numpy import unicode_

def base64decode_from_file(base64file):
    """
    input : file location conatining base 64 text
    output: corrosponding bytes(prints as ASCII)
    """
    with open(base64file) as ct:
        ASCIIbytes = base64.b64decode(ct.read())
    return ASCIIbytes

def hexdecode_from_file(hexfile):
    """
    input : file location conatining hex text
    output: corrosponding bytes(prints as ASCII)
    """
    with open(hexfile) as ct:
        ASCIIbytes = bytes.fromhex(ct.read())
    return ASCIIbytes

def decrypt_aes_ecb(ciphertext, key):
    """
    input:   ciphertext and key in python bytes
    poutput: plaintext in python bytes
    """       

    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def get_blocks_in_list(bytelist, blocksize):
    """
    input: python bytes(ASCIIbytes of a text) object
    output: python byte object sliced into a list of corr block size
    """
    blocks_list = []
    for i in range(0, len(bytelist),blocksize):    
        blocks_list.append(bytelist[i: i+blocksize] )
    return blocks_list

def decrypt_aes_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC,iv=iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')

def PKCS7_padding(plaintext, blocksize):
    """
    input: plaintext that needs to be padded as python bytes object,
            blocksize
    output: padded input as a bytes object
    """
    pt = bytearray(plaintext) #convert to mutable bytearray
    # print(f"plaintext length: {len(plaintext)} bytes")
    extra_bytes = len(plaintext) % blocksize
    # print(f"extra bytes: {extra_bytes} bytes")

    
    pad = blocksize - extra_bytes
    # print(f"padding bytes: {pad} bytes")

    for i in range(pad):
        pt.append(ord(chr(pad)))
    
    # print(bytes(pt))
    return bytes(pt)  

def get_non_unique_blocks(inputbytes, blocksize):
    """
    input: python byte object
        slices the byte string into blocks, 
        and makes a list of non_unique blocks and
        there indices
    output: 2 lists:
            one of non_unique block, each element is a python byte object
            second of their corrosponding indices
    """
    blocks = get_blocks_in_list(inputbytes, blocksize)
    no_of_distinct_blocks = len(set(blocks))
    non_uniques = []
    non_uniques_indices = []
    for i, value in enumerate(blocks):
        if blocks.count(value)>1:
            non_uniques.append(value)
            non_uniques_indices.append(i)
    # print(non_uniques, non_uniques_indices)
    # print(f"non_uniques: {len(non_uniques)}")
    # print(f"distinct blocks: {no_of_distinct_blocks}, total blocks: {len(blocks)} ")
    return non_uniques, non_uniques_indices  

def detect_ecb(ciphertext, blocksize):
    """
    input: a python byte object 
            block-size
    output: tells wheather it's encrypted in ECB mode or not
    """
    #get non uniques:
    a = get_non_unique_blocks(ciphertext, blocksize)
    print("----------")
    print(a)
    if len(a[0])>0:
        # print("ECB moode: TRUE")
        return True
    else:
        # print("ECB mode: FALSE")
        return False
    
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
    key = generate_key(keysize= 16)
    
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

def aes_128_ecb_append(your_string, unkown_string, key):
    """
    Encruption oracle - appends your string to the unknown string and encrypts under ecb mode. Can be used as an encryption oracle.
    
    input: "yourstring" as python byte object
    unkownstring(python bytes): 
    key: 16 byte(128 bit) python byte object

    output: ciphertext
    """
    #making the payload
    
    plaintext = your_string + unkown_string

    #actual encryption oracle
    plaintext = PKCS7_padding(plaintext, 16)
    ciphertext = encrypt_aes_ecb(plaintext,key)
    return ciphertext

