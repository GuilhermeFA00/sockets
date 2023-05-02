import socket
import random

HOST = "127.0.0.1"
PORT = 65432

numero = random.randint(1, 1000)
print(numero)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(int(numero).to_bytes(2, "big"))
    data = s.recv(1024)

print(f"{data!r} FIM")
