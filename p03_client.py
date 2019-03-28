import socket
unix_addr = "file.socket"

# make socket
sk = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
# bind address
sk.sendto("Hello".encode(),unix_addr)
