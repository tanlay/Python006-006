import requests

res = requests.get("https://www.baidu.com")
print(res.status_code)
print(res.headers)
# print(res.text)