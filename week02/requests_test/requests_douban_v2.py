import requests
from pathlib import Path
import sys

"""可以使用sys.exit(0)直接退出程序，而不用执行之后的内容，方便调试"""

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
header = {'user-agent': user_agent}

url = 'https://movie.douban.com/top250'

try:
    resp = requests.get(url, headers=header)
except requests.exceptions.ConnectTimeout as err:
    print(f"requests库连接网络超时, {err}")
    sys.exit(101)
except requests.exceptions.ConnectionError as err:
    print(f"网络错误，请检查网络是否正常 {err}")
    sys.exit(102)

# 内容保存为文件, 
# __file__代表当前的脚本文件
p = Path(__file__)
# print(p)

# 当前文件所在目录
pyfile_path = p.resolve().parent
# print(p.resolve())
# print(p.resolve().parent)

# 建立新的目录html
html_path = pyfile_path.joinpath('html')
if not html_path.is_dir():
    Path.mkdir(html_path)
page = html_path.joinpath('douban.html')


# 上下文管理器
try:
    with open(page, 'w', encoding='utf-8') as f:
        f.write(resp.text)
except FileNotFoundError as err:
    print(f"没有这个文件 {err}")
except IOError as err:
    print(f"文件读写出错 {err}")
except Exception as err:
    print(err)