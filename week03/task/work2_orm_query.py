import sys
from datetime import datetime

import pymysql
from sqlalchemy import (Boolean, Column, Date, DateTime, Integer, MetaData,
                        SmallInteger, String, Table, Text, create_engine, desc,
                        exc, func)
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

# 查看数据
# 查看所有用户名
print(f"查看所有用户名: {[res for res in session.query(Userinfo_table.user_name)]}")
# limit 限制查看用户名
print(f"limit限制查询： {[res for res in session.query(Userinfo_table.user_name).limit(2)]}")
# 降序查询，通过user_age降序查询
print(f"order_by降序： {[res for res in session.query(Userinfo_table.user_name).order_by(desc(Userinfo_table.user_age))]}")
# where条件查询
print([res for res in session.query(Userinfo_table.user_name,Userinfo_table.user_age,Userinfo_table.user_edu).filter(Userinfo_table.user_name == "小明")])
# 统计记录数count(*)
print(f"一共有{[res for res in session.query(func.count(Userinfo_table.user_name)).first()]}条记录")

# 自定义显示查询字段
for res in session.query(Userinfo_table):
    print(res.user_id,res.user_name, res.user_age, res.user_birth, res.user_sex, res.user_edu)