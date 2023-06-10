#!/usr/bin/env python

from pwn import xor

# Given string
given_string = "label"

# XOR each character with the integer 13
xored_string = xor(given_string, 13)

# Convert the resulting integers back to a string
new_string = ''.join(chr(x) for x in xored_string)

# Create the flag format
flag = "crypto{" + new_string + "}"

# Print the flag
print(flag)
