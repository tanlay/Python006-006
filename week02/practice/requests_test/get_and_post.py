import requests


# get方法
resp = requests.get('https://www.github.com')
print(resp.status_code)
print(resp.headers['content-type'])
print(resp.encoding)

#post方法
data = {'key1': 'value1'}
resp = requests.post('https://www.httpbin.org/post', data=data)
print(resp.json())