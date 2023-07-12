#cryptoPals set 1 challenge 1
# hex to base 64
text = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

print(bytes.fromhex(text))
# print(str(text))
# text = "1b70435152891b56f37a80a0de2c3b6f"
#imp: bin() and int() methods
#define hexadecimal value
hex_value = "4"
#convert to Integer(decimal)
int_value = int(hex_value, base=16)
print(int_value)

#convert integer to binary value
bin_value = bin(int_value)
print(f"bin_value: {bin_value}")

#remove the precedding 0b
bin_value = bin(int_value)[2:]
# print(f"bin_value without preceeding 0b: {bin_value}")

#pad for 4 bit string:
bin_value_padded = str(bin(int_value))[2:].zfill(4)
# print(bin_value_padded)

#function to convert base16(or any base) to base2 and pad each hex as 4bit binary number
# 0x4 gets converted to 0b0100 (each hex char gets converted to 4 binary char)
# 0x4 gets converted to 0b00000100 (if padding is 8 bits)

def convertToBinary(ct, radix, padding):
    """
    Converts any radix value into a string representation
    of the corresponding binary value
    Args:
        ct:         the value to be converted, can be hexadecimal, base64 etc
        radix:      the base of the value: 16 if hexadecimal
        padding:    bin() by default displays enough ot represent the most
                    significant bit and omits any leading 0s. Change this to get
                    4-bit binary values or 8-bit binary values
    Returns:
        a str of [padding]-bit binary values of the corrosponding input
        NO:a list of [padding]-bit binary values of the corrosponding input
    """
    bin_ct = []
    for i in ct:
        int_value = int(i, base = radix)
        bin_value = str(bin(int_value))[2:].zfill(padding)
        bin_ct.append(bin_value)
        bin_ct_together = "".join(bin_ct)
    return bin_ct_together




#regroup to 6-bit binary strings
def regroupString(input,n):
    split_string = []
    # n=6
    for i in range(0, len(input), n):
        split_string.append(input[i:i+n])
        # print(i)
    
    return split_string


# print(b)
# shorter way to do the same thing:
# chunks = [a[i: i+6] for i in range(0, len(a),6 )]

b64_index_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def stringToBase64(text):
    """
    Converts a list of 6-bit binary strings to a list of it's corrosponding base64 
    values
    Args: list of the 6-bit binary strings
    Returns: list of corrosponding base64 values to every 6-bit base 2 value
    """
    c = []
    for i in text:
        binaryChar = int(i,2)
        b64_encoding = b64_index_table[binaryChar]
        c.append(b64_encoding)
    return c





#d is the required text btw
text = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hexTobase64(hexString):
    a = convertToBinary(hexString,16,4)
    b = regroupString(a, 6)
    c = stringToBase64(b)
    d = "".join(c)
    return d

print(hexTobase64(text))

