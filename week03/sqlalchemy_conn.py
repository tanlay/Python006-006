import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

# 打开数据库连接
# 需要创建数据库testdb,并授权新用户python访问
# mysql> grant all on testdb.* to 'python'@'%' identified by 'python123'
# echo=True 开启调试
engine = create_engine("mysql+pymysql://python:python123@localhost:3308/testdb",echo=True)

# 创建元数据
metadata = MetaData(engine)

book_table = Table('book', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    )
author_table = Table('author', metadata,
    Column('id', Integer, primary_key=True),
    Column('book_id', None, ForeignKey('book.id')),
    Column('author_name', String(128), nullable=False),
)

try:
    metadata.create_all()
except Exception as err:
    print(f"create error {err}")
