def xor(a,b):
    """
    ^ operates on integers/decimals), so convert bytes to int first
    """
    c = a ^ b
    return c

hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"

#convert hex to decimal/integer
qdec1 = int(hex1, base=16)
qdec2 = int(hex2, base=16)

#convert int/decimal to binary
qbin1 = bin(qdec1)[2:]
print(len(qbin1))

print(f"hex1 length:{len(hex1)} , it's decimal length:{len(str(qdec1))} ")
print(qdec1)
zdec1 = [int(i, base=16) for i in hex1]
print(zdec1)
# print(len(str(qbin1)))
print(qdec2)

res = hex(xor(qdec1 , qdec2))[2:]
print(res)

if res == "746865206b696420646f6e277420706c6179":
    print("success!")
