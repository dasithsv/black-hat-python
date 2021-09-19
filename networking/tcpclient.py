#!/usr/bin/python3

import socket

host = 'www.google.com'
port = 80


client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((host, port))

client.send((b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"))

response = client.recv(9001)

print(response)
client.close()