import sys
import time
import requests
from bs4 import BeautifulSoup
from sqlalchemy import (Column, DateTime, Integer, SmallInteger, Text,
                        create_engine, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
原先打算使用xpath提取数据，之后发现有部分短评没有星级，会导致数据错乱，
并且星级只能提取到（力荐，推荐，还行，较差，很差），数据库不好处理，
(或许是我打开xpath的方式不对)
star = result.xpath('//div[@class="comment"]/h3/span[2]/span[2]/@title')
content = result.xpath('//div[@class="comment"]/p/span/text()')
short_info = dict(zip(star, content))
所以学习了下bs4语法，使用bs4获取数据--BeautifulSoup--
借鉴了这位同学: https://github.com/zlikun/python-crawler-douban-movie.git
数据保存部分，使用了sqlalchmey的ORM，
存在问题可能，重复执行程序，会追加到数据库中，
想到的办法是: 每次建表之前清空表
"""

def download(url, num):
    HEADERS = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        print(f"开始抓取: {url}")
        return res.text
    except Exception:
        print(f'抓取{num}个页面')
        raise Exception (f"抓取失败: {url}")


def pageparse(html, num):
    soup = BeautifulSoup(html, 'html.parser')

    itemtemp = soup.select('#comments > div.comment-item')
    if len(itemtemp) == 0:
        print('资源不存在')
        print(f'累计抓取{num}个页面')
        sys.exit(404)
    data = []
    for item in itemtemp:
        user = item.select_one(
            'h3 > span.comment-info > a').get_text(strip=True)
        rating = item.select_one('h3 > span.comment-info > span.rating')
        star = None
        if rating is not None:
            star = rating.get('class')[0].replace('allstar', '')
            ctime = item.select_one(
                'h3 > span.comment-info > span.comment-time').attrs['title']
            comment = item.select_one(
                'div.comment > p > span.short').get_text(strip=True)

        data.append({
            'user': user,
            'star': star,
            'comment': comment,
            'ctime': ctime
        })
    print(f"movie_id ({movie_id}): 数据提取完成")
    return data


def savedb(movie_id, data):
    Base = declarative_base()

    # 创建引擎
    dburl = 'mysql+pymysql://python:python123@localhost:3308/douban?charset=utf8mb4'
    engine = create_engine(dburl, echo=False, encoding='utf-8')

    # 定义表表
    class Movie_table(Base):
        __tablename__ = f'movie_{movie_id}'
        id = Column(Integer(), primary_key=True,
                    autoincrement=True, comment='主键ID')
        user = Column(String(50), comment='用户')
        star = Column(SmallInteger(), comment='短评星级')
        comment = Column(Text(), comment='短评内容')
        ctime = Column(DateTime(), comment='短评时间')

        def __repr__(self):
            return f'{self.star}: {self.ctime} - {self.user} # {self.comment}'

    # 创建表
    Base.metadata.create_all(engine)

    # 创建session
    db_session = sessionmaker(bind=engine)
    session = db_session()
    # 使用bulk_insert_mappings批量插入list(dict{})格式的数据
    session.bulk_insert_mappings(Movie_table, data)
    try:
        session.commit()
        print(f"movie_id ({movie_id}): 保存数据完成")
    except Exception as err:
        print(f"保存数据失败")
        raise Exception (f'err')


if __name__ == "__main__":
    # 设置需要抓取的电影ID，通过豆瓣网页获取
    # movie_id='1292720'
    # movie_id='1292064'
    movie_id='27073752'

    # next url偏移量
    offset=0
    # 爬取次数
    num=0
    while 1:
        url = f'https://movie.douban.com/subject/{movie_id}/comments?start={offset}&limit=20&status=P&sort=new_score'
        html = download(url, num)
        result = pageparse(html, num)
        savedb(movie_id, result)

        time.sleep(2)
        print("等待2s，继续爬取")
        num += 1
        offset += 20
