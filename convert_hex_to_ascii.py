#!/usr/bin/env python

import base64

# Given hexadecimal string
given_hex = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

# Convert hex string to bytes
given_bytes = bytes.fromhex(given_hex)

# Decode bytes using ASCII encoding
ascii_string = given_bytes.decode('ascii')

# Print the ASCII string
print(ascii_string)
