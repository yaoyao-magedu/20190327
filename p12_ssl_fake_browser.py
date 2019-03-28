import socket
import ssl
import re
import json
ip_addr = ("fanyi.baidu.com", 443)# ip_addr = ("www.baidu.com", 80)

content = "Help"

sk = socket.socket(socket.AF_INET,  # IP format (Address)
                        socket.SOCK_STREAM,  # data format
                        socket.IPPROTO_TCP)  # data (proto)
w_sk = ssl.wrap_socket(sk)
w_sk.connect(ip_addr)
str_request = "POST /sug?kw="+content+" HTTP/1.1\r\n"
str_request += F"Host: {ip_addr[0]}\r\n"
str_request += "Accept: application/json, text/javascript, */*; q=0.01\r\n"
str_request += 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36\r\n'
# str_request += "Accept-Encoding: gzip, deflate, br\r\n"
str_request += "Connection: keep-alive\r\n"
str_request += "Content-Type: application/x-www-form-urlencoded\r\n"
str_request += "\r\n\r\n"

# send data
w_sk.send(str_request.encode("utf-8"))

buf_1 = b""
#recv

while True:
    buf = w_sk.recv(4 * 1024, 0)
    if not buf:
        break
    buf_1 += buf
buf_1 = buf_1.decode()
# print(buf_1)
pattern = re.compile(".+(\[.+\]).+", re.DOTALL)
# buf_2 = re.search(r"\s([{\[].*?[}\]])$", buf_1).group(1)
buf_2 = pattern.match(buf_1).group(1)
print(json.loads(buf_2)[0])