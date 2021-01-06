from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(200), index=True)

    def __repr__(self):
        return f"Book_table(book_id={self.book_id},book_name-={book_name})"
    

class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(50),nullable=False, unique=True)
    created_time = Column(DateTime(), default=datetime.now())
    updated_time = Column(DateTime(), default=datetime.now(), onupdate=datetime.now)

# 实例化引擎
dburl = "mysql+pymysql://python:python123@localhost:3308/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding='utf-8')

# 创建一个session
sessionClass = sessionmaker(bind=engine)
session = sessionClass()

#增加数据
book_demo = Book_table(book_name="聊斋志异")
author_demo = Author_table(username="蒲松林")

session.add(book_demo)
session.add(author_demo)
session.commit()