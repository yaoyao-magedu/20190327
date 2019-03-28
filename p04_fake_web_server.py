import socket

ip_addr = ("", 22222)

sk = socket.socket(socket.AF_INET,  # IP format (Address)
                        socket.SOCK_STREAM,  # data format
                        socket.IPPROTO_TCP)  # data (proto)
# bind
sk.bind(ip_addr)

# listen
sk.listen(2)

client_sk, (ip, port) = sk.accept()
print(ip, port)

while True:
    buf = client_sk.recv(4 * 1024, 0)
    if not buf:
        print("Client Out")
        break
    print(buf.decode("utf-8"))