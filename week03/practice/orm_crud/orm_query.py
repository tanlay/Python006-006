from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, desc
from datetime import datetime

Base = declarative_base()

class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(20), index=True)

    def __repr__(self):
        return f"Book_table(book_id is {self.book_id},book_name is {self.book_name})"

class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    created_time = Column(DateTime(), default=datetime.now())
    updated_time = Column(DateTime(), default=datetime.now(), onupdate=datetime.now)

    def __repr__(self):
        return f"Author_table(user_id is {self.user_id}, username is {self.username})"

# 创建一个实例
dburl = "mysql+pymysql://python:python123@localhost:3306/testdb?charset=utf8mb4" 
engine = create_engine(dburl, echo=False ,encoding='utf-8')

# 创建一个session
sessionClass = sessionmaker(bind=engine)
session = sessionClass()

# 查询数据
# res_book = session.query(Book_table).all()
# print(res_book)
# 可以通过迭代的方式获取数据, 尽量使用迭代代替all()
for result in session.query(Book_table):
    print(result)
# 获取第一个结果
res_author = session.query(Author_table).first()
# one
# scalar
print(res_author)

# 优化查询列,限定列数，默认是select * 
session.query(Book_table.book_name).first()

# 排序
for res_order_by in session.query(Book_table).order_by(Book_table.book_id):
    print(res_order_by)
# 降序
for res_order_by1 in session.query(Book_table).order_by(desc(Book_table.book_id)):
    print(res_order_by1)

# 限制返回条数。Limit
res_limit = session.query(Book_table).limit(2)
print([result.book_name for result in res_limit])

session.commit()