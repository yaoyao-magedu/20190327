import socket
import ssl
ip_addr = ("", 9999)

# make socket
sk = socket.socket(socket.AF_INET,  # IP format (Address)
                        socket.SOCK_STREAM,  # data format
                        socket.IPPROTO_TCP)  # data (proto)
# bind address
sk.bind(ip_addr)

sk.listen(2)

client_sk, (ip, port) = sk.accept()


str_response = "HTTP/1.1 401 Unauthorized\r\n"
str_response += "WWW-Authenticate: Basic realm=\"Example\r\n\"\r\n"
str_response += "Connection: Keep-Alive\r\n"
str_response += "Keep-Alive: 115\r\n"
str_response += "\r\n"

client_sk.send(str_response.encode("utf-8"), 0)
print(ip)
print(port)
while True:
    buf = client_sk.recv(1024 * 4)
    if not buf:
        break
    print(buf.decode())

client_sk.close()
sk.close()
