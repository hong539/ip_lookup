import requests

response = requests.get('https://http2.pro/api/v1', verify=False)
print(response.content)