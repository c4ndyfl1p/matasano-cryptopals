
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


def find_one_byte_of_unknown_string(idx, probable_pt, block_number, unknown_string, key):  
    """Funcion to find the one byte of the unknows string in a AES-ECB mode encrypted block using a encryption oracle.


    Args:
        idx (_type_): _description_
        probable_pt (_type_): _description_
        block_number (_type_): _description_
        unknown_string (_type_): initialised in the encryption oracle itself
        key (_type_): inilialised in the encyrption oracle itself

    Returns:
        _type_: _description_
    """

    if block_number == 0:
        res2 = aes_128_ecb_append( b"AAAAAAAAAAAAAAAA"[0:-idx], base64.b64decode(unknown_string), key) # only 15 bytes
    elif block_number !=0:
        res2 = aes_128_ecb_append( b"AAAAAAAAAAAAAAAA"[0:-idx], base64.b64decode(unknown_string), key) # only 15 bytes

    a2 = get_blocks_in_list(res2,16)
    print(a2)
    last_ct = a2[block_number][-1]
    print(f"last_ct: {last_ct}, hex(last_ct): {hex(last_ct)}")

    #iterate over the last byte of the unknown string from a-z and A-Z and store the result in a dictionary
    possible_chars = [10] + [i for i in range(32, 91)] + [i for i in range(97, 123)]
    for i in possible_chars:
        # print(i)
        
         
        payload = b"AAAAAAAAAAAAAAAA"[0:-idx] + probable_pt + bytes([i])
        print(f"I'm encrypting: {get_blocks_in_list(payload, 16)}") 
        testing_ct = aes_128_ecb_append( payload, base64.b64decode(unknown_string), key)
        
        
        test1 = get_blocks_in_list(testing_ct,16)
        test2 = test1[block_number][-1]

        # if test2 == last_ct:
        if a2[block_number]==test1[block_number]:
            # print(f"test2: {test2}, hex(test2): {hex(test2)}")
            # print(bytes([i]))
            print(f"last byte of unknown string: {i}, chr(i):{chr(i)}, hex(i):{hex(i)}, ord(chr(i)):{ord(chr(i))}")
            # probable_pt = bytes([i])
            break
    return bytes([i])




def find_one_block(prev_decrypted_blocks, block_number):
    """Funcion to find the one block of the unknows string in a AES-ECB mode encrypted block using a encryption oracle.

    Args:
        prev_decrypted_blocks (_type_): _description_
        block_number (_type_): _description_

    Returns:
        _type_: _description_
    """
    probable_pt_concat = prev_decrypted_blocks
    print(f"probable_pt_concat: {probable_pt_concat}")
    for i in range(1,17):
        probable_pt = find_one_byte_of_unknown_string(i, probable_pt_concat, block_number)
        probable_pt_concat += probable_pt
    return probable_pt_concat



# 1. Feed identical bytes of your-string to the function 1 at a time --- 
# start with 1 byte ("A"), then "AA", then "AAA" and so on. Discover the 
# block size of the cipher. You know it, but do this step anyway.
def detect_block_size(unknown_string, key):
    """ # should be independednt of chaining mode or block cipher
    # steps:
    # 1. count the size of the ciphertext
    # 2. Keep adding A's in the begining and querying the oracle until size changes. When size changes:
    # 3. the block size is the difference between the two sizes    
    
    Args:
        unknown_string (_type_): _description_
        key (_type_): _description_

    Returns:
        size (_int_): size of a block, unit is (byte). 
    """
   
    
    original_size = len(aes_128_ecb_append(b"", base64.b64decode(unknown_string), key)) 
    # print(f"original size of ciphertext: {original_size} bytes")

    # add A's and query oracle until size changes
    new_size = len(aes_128_ecb_append(b"", base64.b64decode(unknown_string), key))
    mystring = b'A'
    while (original_size==new_size):        
        new_size = len(aes_128_ecb_append(mystring, base64.b64decode(unknown_string), key))
        mystring = mystring + b'A'

    # print(f"new size of ciphertext: {new_size} bytes")
    
    blocksize = new_size - original_size
    return blocksize


def verify_pkcs7_padding(unknown_input_string):
    if unknown_input_string[-unknown_input_string[-1]:] == bytes([unknown_input_string[-1]]) * unknown_input_string[-1]:
        # strip off the padding and return
        val = unknown_input_string[:-unknown_input_string[-1]]
        return val
    else:
        raise Exception("Invalid PKCS#7 padding")
    
