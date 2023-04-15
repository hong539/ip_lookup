import http.client

conn = http.client.HTTPSConnection("www.cloudflare.com")

conn.request("GET", "/")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))