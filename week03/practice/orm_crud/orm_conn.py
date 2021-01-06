from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()


class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(20), index=True)


class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(128), nullable=False, unique=True)
    created_time = Column(DateTime(), default=datetime.now)
    updated_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


# 实例化一个引擎
dburl="mysql+pymysql://python:python123@localhost:3308/testdb?charset=utf8mb4"
engine=create_engine(dburl, echo=True, encoding="utf-8")

# Base.metadata.create_all(engine)

# 创建一个session
sessionClass = sessionmaker(bind=engine)
session = sessionClass()

session.commit()