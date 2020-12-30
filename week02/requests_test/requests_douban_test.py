import requests
import sys
from pathlib import Path

# 定义变量
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
header = {'user-agent': user_agent}
url = 'https://movie.douban.com/top250'

try:
    resp = requests.get(url, headers=header, timeout=10)
except requests.exceptions.ConnectionError as err:
    print(f"网络错误请检查 {err}")
    sys.exit(101)
except requests.exceptions.ConnectTimeout as err:
    print(f"网络超时 {err}")
    sys.exit(102)

# print(resp.text)

# 保存为文件,当前目录创建子目录html
p = Path(__file__)
cur_path = p.resolve().parent
html_path = cur_path.joinpath('html')
print(html_path)
if not html_path.is_dir():
    Path.mkdir(html_path)

html_page = html_path.joinpath('douban_test.html')
try:
    with open(html_page, 'w', encoding='utf-8') as f:
        f.write(resp.text)
except FileNotFoundError as err:
    print(f"文件没有找到 {err}")
    sys.exit(201)
except IOError as err:
    print(f"文件读写错误 {err}")
    sys.exit(202)
except Exception as err:
    print(err)