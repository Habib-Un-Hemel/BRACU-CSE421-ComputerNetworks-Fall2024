import socket

def count_vowels(message):
    vowels = "aeiouAEIOU"
    return sum(1 for char in message if char in vowels)

def start_server():
    host = '0.0.0.0'
    port = 5001     

    ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser_socket.bind((host, port))
    ser_socket.listen()
    print(f"Server started & listening on {host}:{port}")

    while True:
        cli_socket, cli_address = ser_socket.accept()
        print(f"connected to the client at {cli_address}")
           
        while True:
            message = cli_socket.recv(500).decode('utf-8')  
            if not message:
                print(f"Connection closed by client {cli_address}")
                break

            print(f"Received at {cli_address}: {message}")

            if message.lower() == 'exit':
                print(f"Client {cli_address} requested to close connection.")
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

start_server()