# ip_lookup
For ip_lookup with some Public or Private API 

## How to use?
python version >= 3.8.15
pip install requests
pip install ipwhois

```shell
pipenv shell
python src/*.py
```

## check protocol

```shell
#請問Chrome的開發者工具（DevTools）/Network介面顯示的protocol
#出現h3或h2表示哪些資訊?

#在 Chrome 的開發者工具（DevTools）中的 Network 頁面，如果出現 h2 或 h3，表示該請求使用的是 HTTP/2 或 HTTP/3 協議，而不是 HTTP/1.1 協議。HTTP/2 和 HTTP/3 都是新一代的網路協議，相較於 HTTP/1.1 具有更好的效能和安全性。其中，HTTP/2 支援流、多路徑、優先級、壓縮等功能，而 HTTP/3 則是基於 QUIC 協議，使用 UDP 傳輸，並且使用 TLS1.3 加密。
```



## Reminder!!!
Create codes with ChatGPT

该代码使用了一个名为ip-api.com的API，该API可以通过IP地址查找城市和国家。在该函数中，我们首先构建了URL，然后使用requests模块发送GET请求来获取JSON格式的响应。最后，我们提取响应中的城市和国家信息，并返回它们。

注意，该API有一定的限制，每个IP地址每分钟只能进行150次查询，所以在使用该代码时要注意不要频繁查询同一个IP地址。

还可以使用其他的IP查找API，例如ipstack.com和ipinfo.io等，但这些API可能需要您注册并获取API