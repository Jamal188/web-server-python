import socket 
from render import request_handler, read_request, get_handle

HOST="127.0.0.1"
PORT=9000
NB_OF_CONNECTIONS=2
RESPONSE=b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 15

<h1>Hello!</h1>""".replace(b"\n", b"\r\n")


with socket.socket() as server_socket :
    # resusing some sockets in the system
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((HOST, PORT))

    server_socket.listen(NB_OF_CONNECTIONS)
    
    print("listening .. ")
    
    while True :

        client_sock, client_addr = server_socket.accept()
        request = client_sock.recv(1024).decode()
        print(request)
        with client_sock:
            response_encoded = request_handler(request)
            client_sock.sendall(response_encoded)

            



