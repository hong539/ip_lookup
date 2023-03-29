# ip_lookup
For ip_lookup with some Public or Private API 

## How to use?
python version >= 3.8.15
pip install requests

```shell
python src/main.py
```

## Reminder!!!
Create codes with ChatGPT

该代码使用了一个名为ip-api.com的API，该API可以通过IP地址查找城市和国家。在该函数中，我们首先构建了URL，然后使用requests模块发送GET请求来获取JSON格式的响应。最后，我们提取响应中的城市和国家信息，并返回它们。

注意，该API有一定的限制，每个IP地址每分钟只能进行150次查询，所以在使用该代码时要注意不要频繁查询同一个IP地址。

还可以使用其他的IP查找API，例如ipstack.com和ipinfo.io等，但这些API可能需要您注册并获取API