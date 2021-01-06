import sys
from datetime import datetime

import pymysql
from sqlalchemy import (Boolean, Column, Date, DateTime, Integer, MetaData,
                        SmallInteger, String, Table, Text, create_engine, exc)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Userinfo_table(Base):
    __tablename__ = 'userinfo'
    user_id = Column(Integer(), primary_key=True, doc="主键", comment="主键")
    user_name = Column(String(50), nullable=False, index=True,
                       unique=True, doc="用户名", comment="用户名")
    user_age = Column(SmallInteger(), doc="用户的年龄", comment="用户的年龄")
    user_birth = Column(Date(), doc="用户的出生日期", comment="用户的出生日期")
    # sex使用布尔型表示，男为0，女为1
    user_sex = Column(Boolean(), doc="用户的性别", comment="用户的性别, 男性为0，女性为1")
    user_edu = Column(Text(), doc="用户的学历", comment="用户的学历")
    created_time = Column(DateTime(), default=datetime.now(),
                          doc="用户新增的时间", comment="用户新增的时间")
    updated_time = Column(DateTime(), default=datetime.now(
    ), onupdate=datetime.now, doc="用户信息修改时间", comment="用户信息修改时间")

    def __repr__(self):
        return f"Userinfo_table(user_id is {self.user_id}, user_name is {self.user_name})"


# 创建一个引擎
dburl = "mysql+pymysql://python:python123@localhost:3308/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=False, encoding='utf-8')

# 创建一个session
sessionClass = sessionmaker(bind=engine)
session = sessionClass()

# 准备数据
user1 = Userinfo_table(user_name='猪大明', user_age=30,
                       user_birth='1991-06-17', user_sex=0, user_edu="山东蓝翔")
user2 = Userinfo_table(user_name="热萌檬", user_age=31,
                       user_birth='1990-08-23', user_sex=1, user_edu="北大青鸟")
user3 = Userinfo_table(user_name="小贱土", user_age=36,
                       user_birth='1989-05-29', user_sex=0, user_edu="马津大学")

# 添加数据
session.add(user1)
session.add(user2)
session.add(user3)

try:
    session.commit()
    print(user1, user2, user3)
except exc.SQLAlchemyError:
    print("Insert error")
    sys.exit(99)
