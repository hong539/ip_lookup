import hyper

# 創建一個 HTTP/2 客戶端
client = hyper.HTTP20Connection('www.example.com')

# 向伺服器發送 HTTP/2 請求
client.request('GET', '/')

# 等待伺服器的回應
response = client.get_response()

# 打印伺服器的回應
print(response.read())