#!/usr/bin/env python

import sys
from Crypto.Util.number import long_to_bytes

# Given integer
given_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the integer to bytes and decode to string
message = long_to_bytes(given_integer, sys.byteorder).decode()

# Print the message
print(message)
