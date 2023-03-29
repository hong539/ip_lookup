import socket
from ipwhois import IPWhois

def ip_lookup(ip_address):
    try:
        # 透過 Socket 庫取得 IP 位址的主機名稱
        hostname = socket.gethostbyaddr(ip_address)[0]

        # 使用 ipwhois 庫取得 IP 位址的 WHOIS 資訊
        whois = IPWhois(ip_address)
        # result = whois.lookup_rdap(depth=1)
        result = whois.lookup_rdap()

        # 回傳 result
        return result
        # # 回傳 IP 位址、主機名稱、地理位置資訊、WHOIS 資訊等相關資訊
        # return {
        #     "ip_address": ip_address,
        #     "hostname": hostname,
        #     "country": result["asn_country_code"],
        #     "region": result["network"]["name"],
        #     "city": result["network"]["city"],
        #     "latitude": result["network"]["latitude"],
        #     "longitude": result["network"]["longitude"],
        #     "timezone": result["network"]["timezone"],
        #     "whois": result["objects"],
        # }
    except:
        return None

# 測試範例
ip_address = "1.1.1.1"
result = ip_lookup(ip_address)

print("show result:", result)

# if result:
#     print(f"IP address: {result['ip_address']}")
#     print(f"Hostname: {result['hostname']}")
#     print(f"Location: {result['city']}, {result['region']}, {result['country']}")
#     print(f"WHOIS: {result['whois']}")
# else:
#     print(f"Unable to lookup IP address {ip_address}")