import requests

url = "https://www.google.com"

response = requests.head(url)

print(response.headers['server'])
print(response.raw.version)