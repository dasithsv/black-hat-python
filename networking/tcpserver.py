#!/usr/bin/python3

import socket
import threading

ip = '0.0.0.0'
port = 9004

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind ((ip, port))
    server.listen(5)
    print(f'[*] Listning on {ip}:{port}')

    while True:
        try:
            # we get the client socket on client and connection details on address -> address can be something like ('127.0.0.1', 41410)
            client, address = server.accept() 
            print(f"[*] Got connection from {address[0]}:{address[1]}")

            # create a new Thread object that points to handle_client funtion and we pass client ip as argument
            client_handler = threading.Thread(target=handle_client, args=(client,)) 
            client_handler.start()
        except:
            print('[-] Something went wrong')
            socket.close()
            exit()

def handle_client(client_socket):
    # do a recv and then send a simple message back
    with client_socket as sock:
        try:
            request = sock.recv(1024)
            print(f"[*] Received : {request.decode('utf-8')}")
            sock.send(b'got it! ')
        except:
            print("[-] Something went wrong")
            exit()

if __name__ == '__main__':
    main()