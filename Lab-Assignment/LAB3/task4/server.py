import socket

def calculate_salary(hours):
    if hours<=40:
        return (hours*200)
    else:
        return 8000+(hours-40)*300

def start_server():
    host = '0.0.0.0'
    port = 5003     
    ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser_socket.bind((host,port))
    ser_socket.listen()
    print(f"Server started and listening on {host}:{port}")
    while True:
        cli_socket, cli_address = ser_socket.accept()
        print(f"Connected to client at {cli_address}")
        while True:
            message = cli_socket.recv(500).decode('utf-8')
            if not message:
                print(f"Connection closed by client {cli_address}")
                break
            print(f"Received from {cli_address}: {message}")
            if message.lower() == 'exit':
                print(f"Client {cli_address} requested to close the connection.")
                break
            salary = calculate_salary(int(message))  
            response = f"Your salary is {salary}"
            cli_socket.send(response.encode('utf-8')) 
            print(f"Sent to {cli_address}: {response}") 

start_server()