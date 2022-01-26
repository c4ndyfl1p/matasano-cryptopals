
def PKCS7_padding(plaintext, blocksize):
    """
    input: plaintext that needs to be padded as python bytes object,
            blocksize
    output: padded input as a bytes object
    """
    pt = bytearray(plaintext) #convert to mutable bytearray
    pad = blocksize - (len(pt) % blocksize)

    for i in range(pad):
        pt.append(ord(chr(pad)))
    return bytes(pt)


p = b"YELLOW SUBMARINE"
print(PKCS7_padding(p, 16))