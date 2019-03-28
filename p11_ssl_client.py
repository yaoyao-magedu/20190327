import socket
import ssl
# 构建上下文环境 context
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# load cert
ctx.load_verify_locations("cert/ca.crt")

# make socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
# patch socket
w_sk = ctx.wrap_socket(sock=sk, server_hostname="SERVER")
# data by encrypted

w_sk.connect(("localhost", 8443))
while True:
    w_sk.send("Hello".encode(), 0)
