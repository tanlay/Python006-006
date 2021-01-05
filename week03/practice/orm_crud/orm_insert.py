from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime
from datetime import datetime

# 打开数据库连接
Base = declarative_base()

class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True,unique=True)
    book_name = Column(String(50), index=True)

    def __repr__(self):
        return "Book_table(book_id='{self.book_id}'," \
            "book_name={self.book_name})".format(self=self)

class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_time = Column(DateTime(), default=datetime.now())
    updated_time = Column(DateTime(), default=datetime.now(), onupdate=datetime.now)

# 实例化一个引擎
dburl = "mysql+pymysql://python:python123@localhost:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
book_demo = Book_table(book_name="百年孤独")
# author_demo = Author_table()
# print(book_demo)
# print(author_demo)
session.add(book_demo)
session.commit()