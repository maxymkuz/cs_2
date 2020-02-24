from urllib import request


print(dir(request))

resp = request.urlopen("https://www.wikipedia.org/")

print(resp.code)
print(resp.length)
print(resp.peek())
data = resp.read()
print(data)
html = data.decode("UTF-8")
print(html)