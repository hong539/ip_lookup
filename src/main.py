import requests

def ip_lookup(ip_address):
    url = 'http://ip-api.com/json/' + ip_address
    response = requests.get(url).json()
    city = response['city']
    country = response['country']
    return city, country

ip_address = '8.8.8.8'  # 要查询的IP地址
city, country = ip_lookup(ip_address)
print(f"The IP address {ip_address} is located in {city}, {country}.")