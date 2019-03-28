import socket
import ssl
# 构建上下文环境 context
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

ctx.load_cert_chain(
    certfile="cert/server.crt",
    keyfile="cert/server_rsa_private.pem",
    password="server")

# make socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
# patch socket
w_sk = ctx.wrap_socket(sock=sk, server_side=True)
# data by encrypted

w_sk.bind(("", 8443))

w_sk.listen(2)
client, (ip, port) = w_sk.accept()
print("Link", ip, port)
while True:
    buf = client.recv(4 * 1024, 0)
    print(buf)
    if not buf:
        break

