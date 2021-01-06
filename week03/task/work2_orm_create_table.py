from datetime import datetime

import pymysql
from sqlalchemy import (Boolean, Column, Date, DateTime, Integer, MetaData,
                        SmallInteger, String, Table, Text, create_engine)

dburl = "mysql+pymysql://python:python123@localhost:3308/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=False, encoding='utf-8')

# 创建元数据
metadata = MetaData(engine)

userinfo_table = Table('userinfo', metadata,
                       Column("user_id", Integer(), primary_key=True, doc="主键", comment="主键"),
                       Column("user_name", String(50), nullable=False, index=True, unique=True, doc="用户名", comment="用户名"),
                       Column("user_age", SmallInteger(), doc="用户的年龄", comment="用户的年龄"),
                       Column("user_birth", Date(), doc="用户的出生日期", comment="用户的出生日期"),
                       Column("user_sex", Boolean(), doc="用户的性别", comment="用户的性别, 男性为0，女性为1"),
                       Column("user_edu", Text(), doc="用户的学历", comment="用户的学历"),
                       Column("created_time", DateTime(), default=datetime.now(), doc="用户新增的时间", comment="用户新增的时间"),
                       Column("updated_time", DateTime(), default=datetime.now(), onupdate=datetime.now, doc="用户信息修改时间", comment="用户信息修改时间"),
                       )

try:
    metadata.create_all()
except Exception as err:
    print(f"create table error {err}")
