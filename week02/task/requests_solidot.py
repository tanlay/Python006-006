"""
使用requests抓取solidot.org上 云计算 模块新闻
"""
import sys
import requests
from lxml import etree
from fake_useragent import UserAgent
from pathlib import Path

# # 定义变量
# web_url = 'https://cloud.solidot.org/'
# ua = UserAgent(verify_ssl=False)
# header = {'user-agent': ua.random}

# res = requests.get(web_url, headers=header)
# # print(res.text)

# # 使用xpath提取新闻相关信息
# selector1 = etree.HTML(res.text)
# new_name = selector1.xpath('//div[@class="bg_htit"]/h2/a/text()')
# # new_time = selector.xpath('//div[@class="talk_time"]/text()[3]')
# new_text_urls = selector1.xpath('//div[@class="talkm_mid"]/div[@class="l"]/a/@href') 
# # 取得new的新闻内容地址
# # new_url = []
# # for new_text_url in new_text_urls:
# #     new_text_url = web_url + new_text_url
# #     new_url.append(new_text_url)
# # print(new_url)

# new_info = dict(zip(new_name, new_text_url))
# # for name, time in new_info.items():
# print(new_info)


class getSolidotNew():
    def __init__(self):
        self.ua = UserAgent(verify_ssl=False)
        self.header = {'user-agent': self.ua.random}
        # self.crawl_url = 'https://linux.solidot.org/'
        self.crawl_url = 'https://cloud.solidot.org/'

    def get_news_info(self):
        resp = requests.get(self.crawl_url, headers=self.header)
        selector = etree.HTML(resp.text)
        news_name = selector.xpath('//div[@class="bg_htit"]/h2/a/text()')
        # new_text_url = selector.xpath('//div[@class="talkm_mid"]/div[@class="l"]/a/@href')
        news_time = selector.xpath('//div[@class="talk_time"]/text()[3]')
        news_info = dict(zip(news_name,news_time))
        return news_info

    def to_file(self, path):
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(str(result))
        except FileNotFoundError as err:
            print(f"没有找我该文件 {err}")
        except IOError as err:
            print(f"文件读写错误 {err}")
        except Exception as err:
            print(err)

if __name__ == "__main__":
    p = Path(__file__)
    # 获取当前目录的父目录
    cur_path = p.resolve().parent
    # 文件存放位置
    save_file = cur_path.joinpath('solidot_cloud.json')

    news = getSolidotNew()
    result = news.get_news_info()
    news.to_file(save_file)