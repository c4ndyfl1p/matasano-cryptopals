import string 

a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
a = "91ad79072521c2454de5733742478e4c"
# print(len(a))
# aDEcode = bytearray.fromhex(a).decode()
# print(aDEcode)

# b = list of 4 bit binary strings
b = [ bin(int(i, base=16))[2:].zfill(4) for i in a]
# print(*b)

#regroup to a byte

c= "".join(b)
# print(c)

#d has one byte
#d = list of 8 bit/1byte binary strings
d = []
for i in range(0, len(c), 8):
    d.append(c[i:i+8])

# print(*d)

#each byte of the list converted to an integer
e = [ int(i, base=2) for i in d]
print(*e)

teste = [int(i, base=16) for i in a]
print(*teste)

# each integer of the converted t its corrosponding ACII symbol
f = [chr(i) for i in e]
# print(*f)
print(f)


#do the xor
def do_xor(input_list, key):
    output_list = []
    for i in input_list:
        j = chr(i ^ key)
        output_list.append(j)
        outString= "".join(output_list)                
    return outString, key

# print(do_xor(e, 1))

for i in range(256):
    print(do_xor(e, i))
    
# keys = [i for i in keys]


