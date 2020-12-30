import requests
from lxml import etree
import time

"""
处理翻页
通过time.sleep控制请求频率
"""


def get_url_name(url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    header = {'user-agent': user_agent}
    resp = requests.get(url, headers=header)

    selector = etree.HTML(resp.text)
    # 电影名称列表
    film_name = selector.xpath('//div[@class="hd"]/a/span[1]/text()')
    print(film_name)

    # 电影链接列表
    film_link = selector.xpath('//div[@class="hd"]/a/@href')
    print(film_link)

    # 遍历对应关系生成字典
    film_info = dict(zip(film_name, film_link))
    # for i in film_info:
    #     print(f'电影名称: {i}\t\t 电影链接： {film_info[i]}')
    for name,link in film_info.items():
        print(f'电影名称: {name}\t\t 电影链接： {link}')


if __name__ == "__main__":
    urls = tuple(
        f'http://movie.douban.com/top250?start={ page * 25}&filter=' for page in range(10))
    # print(urls)

    for page in urls:
        get_url_name(page)
        time.sleep(3)
