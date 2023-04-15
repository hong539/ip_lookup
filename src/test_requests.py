import requests

response = requests.get('https://google.com')
print(response.raw.version)