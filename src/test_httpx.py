import httpx

url = "https://http2.pro/api/v1"
headers = {"Accept": "application/json"}

with httpx.Client(http2=True) as client:
    response = client.get(url, headers=headers)

print(response.status_code)
print(response.text)