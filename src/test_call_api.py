import socket
import requests

def ip_lookup(ip_address):
    try:
        # 透過 Socket 庫取得 IP 位址的主機名稱
        hostname = socket.gethostbyaddr(ip_address)[0]

        # 透過網站 API 取得 IP 位址的地理位置資訊
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()

        # 回傳 IP 位址、主機名稱、地理位置資訊等相關資訊
        return {
            "ip_address": ip_address,
            "hostname": hostname,
            "country": data["country"],
            "region": data["regionName"],
            "city": data["city"],
            "zip_code": data["zip"],
            "latitude": data["lat"],
            "longitude": data["lon"],
            "timezone": data["timezone"],
        }
    except:
        return None

# 測試範例
ip_address = "8.8.8.8"
result = ip_lookup(ip_address)
if result:
    print(f"IP address: {result['ip_address']}")
    print(f"Hostname: {result['hostname']}")
    print(f"Location: {result['city']}, {result['region']}, {result['country']}")
else:
    print(f"Unable to lookup IP address {ip_address}")