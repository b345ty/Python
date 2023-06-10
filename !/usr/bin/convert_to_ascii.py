!/usr/bin/env python

# Import the necessary module
import sys

# Given integer array
integer_array = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Convert integers to ASCII characters and join them
ascii_string = ''.join(chr(num) for num in integer_array)

# Print the ASCII string
print(ascii_string)
