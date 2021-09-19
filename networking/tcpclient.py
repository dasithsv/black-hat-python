#!/usr/bin/python3
import socket

host = 'www.google.com'
port = 80

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

'''
Create socket object with AF_INET and SOCK_STREAM 

- The AF_INET parameter indicates we’ll use a standard IPv4 address or host-name 
- SOCK_STREAM indicates that this will be a TCP client 
'''

client.connect((host, port))
# connecting to the host and port

client.send((b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"))
# just sends a headers for the request

response = client.recv(9001)
# getting the response

print(response.decode())
# printing the resonse

client.close()
# close the connection