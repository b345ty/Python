#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

# Establish a Telnet connection to the specified host and port
tn = telnetlib.Telnet(HOST, PORT)

# Function to read a line from the Telnet connection
def readline():
    return tn.read_until(b"\n")

# Function to receive JSON data from the Telnet connection
def json_recv():
    line = readline()
    return json.loads(line.decode())

# Function to send JSON data to the Telnet connection
def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

# Print the initial lines received from the Telnet connection
print(readline())
print(readline())
print(readline())
print(readline())

# Send a request to buy guns
request = {
    "buy": "guns"
}
json_send(request)

# Receive the response
response = json_recv()

# Print the received response
print(response)
