import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"{addr}")

        new_data = conn.recv(1024)

        new_data = int.from_bytes(new_data, 'big')

        n = new_data
        count = 0
        while (n > 0):
            count = count + 1
            n = n // 10

        if count > 10:
            new_data = str(new_data)
            conn.sendall(new_data.encode())
        elif count < 10:
            if (new_data % 2) == 0:
                conn.sendall("PAR".encode())
            else:
                conn.sendall("ÍMPAR".encode())
