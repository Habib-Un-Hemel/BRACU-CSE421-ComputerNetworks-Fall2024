import socket
import platform

def send_from_client():
    host = '127.0.0.1'
    port = 5000         
    
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_socket.connect((host, port))
    cli_ip = socket.gethostbyname(socket.gethostname()) 
    device_name = platform.node()
    msg = f"IP: {cli_ip}, Device: {device_name}"
    
    cli_socket.send(msg.encode('utf-8'))
    print("Information send to Server")
    
    cli_socket.close()  

send_from_client()