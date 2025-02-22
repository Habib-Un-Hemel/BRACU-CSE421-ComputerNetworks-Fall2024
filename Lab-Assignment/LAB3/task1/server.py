import socket

def send_from_server():
    host = '0.0.0.0'
    port = 5000       
    
    ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser_socket.bind((host, port))
    ser_socket.listen()
    print(f"server started & listening on {host}:{port} ")
    while True:
        client_socket, client_address = ser_socket.accept()
        print(f"connection established with   {client_address}")
        
        data = client_socket.recv(500).decode('utf-8')  
        print(f"received from client {data}")
        
        client_socket.close() 


send_from_server()