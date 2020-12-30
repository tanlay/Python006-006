import requests

# 在同一个session实例发出的所有请求之前保持cookie
sess = requests.Session()

sess.get("http://www.httpbin.org/cookies/set/sessioncookie/123456789")
resp = sess.get("http://www.httpbin.org/cookies")
print(resp.text)
"""
{
  "cookies": {
    "sessioncookie": "123456789"
  }
}
"""

# 会话也可使用上下文管理器实现
with requests.Session() as sess:
    sess.get("https://www.httpbin.org/cookies/set/sessioncookie/123456789")
