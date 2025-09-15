# client.py
import socket

HOST = 'localhost'
PORT = 8074
print("client is running")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"connected with server successfully {HOST}:{PORT}")
    data = s.recv(1024)

print(f"Message from server: {data.decode()}")