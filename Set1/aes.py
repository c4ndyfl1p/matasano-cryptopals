
from Crypto.Cipher import AES
import base64, binascii

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
    break a stream of bytes into blocks of given size, return that
    """

    """
    input:
        bytelist:_bytes_python bytes(ASCIIbytes of a text) object
        blocksize:_int_ size of each block
    output:_list_ python byte object sliced into a list of corr block size
    """
    blocks_list = []
    for i in range(0, len(bytelist),blocksize):    
        blocks_list.append(bytelist[i: i+blocksize] )
    return blocks_list