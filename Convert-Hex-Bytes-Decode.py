#!/usr/bin/env python

import base64

# Given hexadecimal string
given = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

# Convert the hexadecimal string to bytes
given_bytes = bytes.fromhex(given)

# Encode the bytes in base64 and decode the result to a string
base64_encoded = base64.b64encode(given_bytes).decode()

# Print the base64-encoded string
print(base64_encoded)
