from datetime import datetime

import requests
from bs4 import BeautifulSoup
from sqlalchemy import (Column, DateTime, Integer, SmallInteger, Text,
                        create_engine)
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
数据保存部分，使用了sqlalchmey的ORM来。
"""

def download(url):
    HEADERS = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    try:
        res = requests.get(url, headers=HEADERS, timeout=5)
        print(res)
        return res.text
    except requests.ConnectionError as err:
        print(f'请检查网络！{err}')
    except requests.ConnectTimeout as err:
        print(f'连接超时： {err}')
    except Exception as err:
        print(err)


def pageparse(html):
    soup = BeautifulSoup(html, 'html.parser')

    itemtemp = soup.select('#comments > div.comment-item')
    data = []
    for item in itemtemp:
        user = item.select_one(
            'h3 > span.comment-info > a').get_text(strip=True)
        rating = item.select_one('h3 > span.comment-info > span.rating')
        # print(rating)
        star = None
        if rating is not None:
            star = rating.get('class')[0].replace('allstar', '')
            # print(star)
            ctime = item.select_one(
                'h3 > span.comment-info > span.comment-time').attrs['title']
            # print(ctime)
            # te = []
            comment = item.select_one(
                'div.comment > p > span.short').get_text(strip=True)
            # te.append(comment)
            # print(len(te))

        data.append({
            'user': user,
            'star': star,
            'comment': comment,
            'ctime': ctime
        })

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
        user = Column(Text(), comment='用户')
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
    session.commit()


if __name__ == "__main__":
    # 设置需要抓取的电影ID，通过豆瓣网页获取
    movie_id='1292720'
    # 拼接URL
    url = f'https://movie.douban.com/subject/{movie_id}/comments'
    # 调用download下载相应页面
    html = download(url)
    # 调用pageparse解析需要的数据
    result = pageparse(html)
    # 数据保存数据库
    savedb(movie_id, result)

