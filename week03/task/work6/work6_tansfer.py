"""
张三给李四通过网银转账 100 极客币，现有数据库中三张表：

一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。

创建数据库geek后，通过ORM创建数据表，还需要填充基础数据
INSERT INTO `geek`.`userinfo`(`uid`, `uname`) VALUES (1000001, '张三');
INSERT INTO `geek`.`userinfo`(`uid`, `uname`) VALUES (1000002, '李四');
INSERT INTO `geek`.`assets`(`uid`, `total_amount`) VALUES (1000001, 100.00);
INSERT INTO `geek`.`assets`(`uid`, `total_amount`) VALUES (1000002, 0.95);
"""

import sys
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Index, Integer, String, DECIMAL, DateTime
from datetime import datetime

# 创建一个Base类，之后创建表的类需要继承这个类
Base = declarative_base()

class Userinfo_table(Base):
    __tablename__ = 'userinfo'
    uid = Column(Integer(), primary_key=True, comment='用户ID,主键')
    uname = Column(String(32), nullable=True, index=True, comment='用户名')

    def __repr__(self):
        return (f"userinfo_table({self.uid} name is {self.uname})")


class Assets_table(Base):
    __tablename__ = 'assets'
    uid = Column(Integer(), primary_key=True, comment='用户ID')
    total_amount = Column(DECIMAL(10,2), nullable=False, comment='用户总资产')

    def __repr__(self):
        return (f"Assets_table({self.uid} total assets are {self.total_amount})")


class Record_table(Base):
    __tablename__ = 'record'
    rid = Column(Integer(), primary_key=True, autoincrement=True, comment="主键ID")
    src_id = Column(Integer(), index=True, comment='转账ID')
    des_id = Column(Integer(), index=True, comment='被转账ID')
    amount = Column(DECIMAL(10,2), nullable=False, comment='转账金额')
    ctime = Column(DateTime, default=datetime.now(), comment="转账时间")
    
    def __repr__(self):
        return (f"Assetslog_table({self.src_id} transfers {self.amount} to {self.des_id} at {self.ctime})")

class OpTable():
    # 创建表
    def create_table():
        Base.metadata.create_all(engine)

    # 删除所有表
    def drop_table():
        Base.metadata.drop_all(engine)
    
    def transfer(src, des, fee ,session):
        src_id = session.query(Userinfo_table.uid).filter(Userinfo_table.uname == src).first()[0]
        des_id = session.query(Userinfo_table.uid).filter(Userinfo_table.uname == des).first()[0]
        src_amount = session.query(Assets_table.total_amount).filter(Assets_table.uid == src_id).first()[0]
        des_amount = session.query(Assets_table.total_amount).filter(Assets_table.uid == des_id).first()[0]
        # print(src_id)
        # print(des_id)
        # print(src_amount)
        # print(des_amount)

        src_amount -= fee
        des_amount += fee
        if (src_amount < 0):
            src_amount += fee
            des_amount -= fee
            sys.exit(99)

        session.query(Assets_table.total_amount).filter(Assets_table.uid == src_id).update({Assets_table.total_amount: src_amount})
        session.query(Assets_table.total_amount).filter(Assets_table.uid == des_id).update({Assets_table.total_amount: des_amount})

        result = Record_table(src_id=src_id, des_id=des_id, amount=fee)
        session.add(result)



if __name__ == "__main__":
    # 创建引擎
    dburl = "mysql+pymysql://python:python123@localhost:3308/geek?charset=utf8mb4"
    engine = create_engine(dburl, echo=False, encoding="utf-8")

    # 创建会话
    sessionClass = sessionmaker(bind=engine)
    session = sessionClass()

    # 调用创建表方法
    # OpTable.create_table()
    # 调用删除表方法
    # OpTable.drop_table()
    try:
        # 调用transfer方法
        OpTable.transfer("张三", "李四", 10, session)
        session.commit()
    # except exc.SQLAlchemyError:
    except Exception:
        print(f"Transfer error")
        session.rollback()
    finally:
        session.close()