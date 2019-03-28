import urllib.parse

url = "http://joe:123456@www.baidu.com/download/image.png?name=tom&page=2#anchor"
result = urllib.parse.urldefrag(url)
print(type(result), result, result.url, result.fragment)
re = urllib.parse.urlsplit(result.url)

print(re, type(re))

print(re.username)
print(re.password)
print(re.scheme)
print(re.netloc)

url_2 = "http://baidu.com/index.html?name=姓名&age=23"
r = urllib.parse.quote(url_2)
print(r)

rr = urllib.parse.unquote(r)
print(rr)