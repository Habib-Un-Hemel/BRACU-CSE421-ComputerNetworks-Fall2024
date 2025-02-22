import socket
import threading

def count_vowels(message):
    vowels = "aeiouAEIOU"
    return sum(1 for char in message if char in vowels)

def handle_client(cli_socket, cli_address):
    print(f"New connection from {cli_address}")
    while True:
        message = cli_socket.recv(500).decode('utf-8')  
        if not message:
            print(f"Connection closed by {cli_address}")
            break

        print(f"Received from {cli_address}: {message}")
        
        if message.lower() == 'exit':
            print(f"Client {cli_address} requested to close the connection.")
            break
        
        vowel_count = count_vowels(message)
        if vowel_count == 0:
            response = "Not enough vowels"
        elif vowel_count <= 2:
            response = "Enough vowels I guess"
        else:
            response = "Too many vowels"
        
        cli_socket.send(response.encode('utf-8')) 
        print(f"Sent to {cli_address}: {response}")
def start_server():
    host = '0.0.0.0'
    port = 5002     
    ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser_socket.bind((host, port))
    ser_socket.listen(5) 
    print(f"Server started & listening on {host}:{port}")  
    while True:
        cli_socket, cli_address = ser_socket.accept()

        cli_thread = threading.Thread(target=handle_client, args=(cli_socket, cli_address))
        cli_thread.start()
        
start_server()