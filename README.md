# Matasano-cryptopals

## Set 1

#### Challenge 1:

### Convert hex to base64

  The string:

```
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
```

  Should produce:

```
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```

  So go ahead and make that happen. You'll need to use this code for the rest of the exercises.



-----

Implementation:

1. Convert base hexadecimal to 8bit- binary string
2. regroup the 8bit-base2 string to 6-bit base 2 string
3. convert the 6-bit binary strings to decimals and then map to the base64 table

The code I wrote is quite long and chunky for something so simple, but I wanted to see how different it is if I work exclusively on strings or lists. I also did not want to use the standard library too much.

Functions used : bin(), int()

Takeaway: 

- Any representation of data has 2 aspects: radix/base and length.

  Saying "a binary string" is not enough. Instead "an 8-bit binary string" is more useful.