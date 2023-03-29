import socket
from ipwhois import IPWhois

ip_address = input("Enter IP address or domain name: ")

try:
    ip = socket.gethostbyname(ip_address)
    print("IP address: ", ip)
except socket.gaierror:
    print("Invalid input. Please enter a valid IP address or domain name.")

ipwhois = IPWhois(ip)
results = ipwhois.lookup_rdap()

# print("Country: ", results['asn_country_code'])
# print("City: ", results['city'])
# print("Organization: ", results['asn_description'])