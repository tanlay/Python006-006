import requests
from fake_useragent import UserAgent
import sys

ua = UserAgent(verify_ssl=False)
# print(ua.random)
# 随机生成user_agent

header = {
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login'
}

sess = requests.session()
# 会话对象：在同一个Session实例发出的所有请求之间保持cookie
# 期间使用urllib3的connection pooling功能
# 向同一主机发送多个请求，底层的TCp连接会被重用，从而带来显著的性能提升

login_url = 'https://accounts.douban.com/j/mobile/login/basic'
from_data = {
    'ck':'',
    'remember':'true',
    'name':'XXXXX',
    'password':'*******',
}

resp = sess.post(login_url, data=from_data, headers=header)
print(resp.headers)