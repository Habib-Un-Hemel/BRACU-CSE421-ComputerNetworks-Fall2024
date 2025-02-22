import socket

def start_client():
    ser_host = '127.0.0.1'
    ser_port = 5001  
    
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_socket.connect((ser_host, ser_port))
    print(f"Connected to server at {ser_host}:{ser_port}")
    
    while True:
        message = input("Enter a message to send the server or type 'exit' ") 
        if message.lower() == 'exit':
            print("Closing connection")
            break
        cli_socket.send(message.encode('utf-8'))  
        response = cli_socket.recv(500).decode('utf-8')  
        print(f"server response: {response}")
start_client()