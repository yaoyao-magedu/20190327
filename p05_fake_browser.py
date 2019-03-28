import socket

ip_addr = ("www.baidu.com", 80)# ip_addr = ("www.baidu.com", 80)

sk = socket.socket(socket.AF_INET,  # IP format (Address)
                        socket.SOCK_STREAM,  # data format
                        socket.IPPROTO_TCP)  # data (proto)
sk.connect(ip_addr)

str_request = "GET / HTTP/1.1\r\n"
str_request += F"Host: {ip_addr[0]}\r\n"
str_request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\n"
str_request += 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36\r\n'
# str_request += "Accept-Encoding: gzip, deflate, br\r\n"
str_request += "Connection: keep-alive\r\n"
str_request += "\r\n\r\n"
# send data
sk.send(str_request.encode("utf-8"))

#recv

while True:
    buf = sk.recv(4 * 1024, 0)
    if not buf:
        break

    print(buf.decode("utf-8"))

