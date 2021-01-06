from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import DateTime
from datetime import datetime

Base = declarative_base()


class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(200), nullable=False, index=True)

    def __repr__(self):
        return f"Book_table(book_id is {self.book_id}, book_name is {self.book_name})"


class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    created_time = Column(DateTime(), default=datetime.now())
    updated_time = Column(
        DateTime(), default=datetime.now(), onupdate=datetime.now)

    def __repr__(self):
        return f"Author_table(user_id is {self.user_id}, username is {self.username})"


# 新建引擎
dburl = "mysql+pymysql://python:python123@localhost:3308/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding='utf-8')

# 创建一个session
sessionClass = sessionmaker(bind=engine)
session = sessionClass()

# 更新数据
query = session.query(Book_table)
query = query.filter(Book_table.book_id == 8)
# 传递字典类型的参数
query.update({Book_table.book_name: "newbook"})
new_book = query.first()
print(new_book.book_name)

# 记得使用commit()来做提交操作,否则数据库不会做修改
session.commit()
