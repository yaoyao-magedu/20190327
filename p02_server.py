import socket

ip_addr = ("", 9999)
unix_addr = "file.socket"

# make socket
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# bind address
sk.bind(unix_addr)
# listen

# accept

# make buffer (user agent)

# get data from buffer
while True:
    buf = sk.recv(1024 * 1, 0)
    if not buf:
        break
    print(buf.decode())
