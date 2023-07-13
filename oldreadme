# Matasano-cryptopals

My attempts at doing the Cryptopals challenges in Python.
Having a lot of fun. You should to!

If you happen to find this repository, bewarned, a lot of this code was written after, just 1 semester of python, at the start of my undergrad.
Please be kind :) pretty please.
Set 1, especially might feel unreadbale. I *like* to think I code better now. Emphasis on the like.

I initially wanted to do writeups for all challenges, but that felt more of a task than pleasure. And I ended up procrastinating on even doing the challenges for over a year :)
Now, I might do writeups for just specific challenges where I find something interesting, or if I come across dead end(in hopes that a future me might read them someday, and she'd be smarter than the present me and chuckle at the satisfaction of solving something she could not solve before).


On y va!

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

#### Challenge 2:

Implementation:

Convert both the hexadecimal strings to 