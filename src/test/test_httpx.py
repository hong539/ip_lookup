import httpx

url = "https://www.google.com.tw/"

with httpx.Client(http2=True) as client:
    response = client.get(url)

print(response.http_version)