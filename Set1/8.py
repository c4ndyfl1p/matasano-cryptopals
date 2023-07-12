import base64

from numpy import byte
from aes import * 
import binascii, base64

key = b"YELLOW SUBMARINE"    
hexfile = "Set1/8.txt"

with open(hexfile) as f:
    lines = f.readlines()



print((lines[0]), len(lines))
bytelines = [ bytes.fromhex(line) for line in lines]
# linesint = ["{0:b}".format(int.from_bytes(line, "big")) for line in bytelines]
print(len(bytelines[0])) 
#gives 160. So each string is 160 bytes, so 20 blocks.
# we gotta check if any 2 blocks are same

def detect_ecb(ciphertext, blocksize):
    """
    input: (a python byte object 
            block-size) aes encoded object
    output: tells wheather it's encrypted in ECB mode or not
    """
    blocks = get_blocks_in_list(ciphertext, blocksize)
    distinct_lengths = len(set(blocks))
    if distinct_lengths < len(blocks):
        print("ECB moode: TRUE")
        return ciphertext
    else:
        print("ECB mode: FALSE")
        return False
        

a = [detect_ecb(bytelines[i], 16) for i in range(len(bytelines)) ]
print(a)

blocks = [ get_blocks_in_list(bytelines[i],16) for i in range(len(bytelines))    ]
# print(blocks)
distinct_lengths = [len(set(block)) for block in blocks] #prints how many distint blocks are there 
# print(distinct_lengths)

#get the index of the least distinct, i.e minimum element in distict_lengths

ecb_encrypted = bytelines[distinct_lengths.index(min(distinct_lengths))]
print(ecb_encrypted)

