def xor(a,b):
    c = a ^ b
    return c

hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"

qbin1 = int(hex1, base=16)
qbin2 = int(hex2, base=16)

print(qbin1)
print(qbin2)

res = hex(xor(qbin1 , qbin2))[2:]
print(res)

