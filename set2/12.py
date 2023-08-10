import base64
from pprint import pprint
from aes import *



key = b'dTP\xdc"\xb8\xa4\x12\xe3H\xfc\xd5zS\x02\xf2'
unknown_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"

print(f"length of unknows string is {len(base64.b64decode(unknown_string))}")
# res = aes_128_ecb_append(b"", base64.b64decode(unknown_string), key) # how to use the oracle


def find_one_byte_of_unknown_string(idx, probable_pt, block_number):  
    """Funcion to find the last byte of the unknows string in a AES-ECB mode encrypted block

    Args:
        idx (_type_): _description_
        probable_pt (_type_): _description_
        block_number (_type_): _description_

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
    probable_pt_concat = prev_decrypted_blocks
    print(f"probable_pt_concat: {probable_pt_concat}")
    for i in range(1,17):
        probable_pt = find_one_byte_of_unknown_string(i, probable_pt_concat, block_number)
        probable_pt_concat += probable_pt
    return probable_pt_concat



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

#3-5 decrypted it

blocks_decrypted = b""
for i in range(9):
    blocks_decrypted =  find_one_block(blocks_decrypted, i)

print(blocks_decrypted)