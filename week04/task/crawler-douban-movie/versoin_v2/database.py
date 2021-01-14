from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, DateTime, SmallInteger, Integer, String, Text


def savedb(movie_id, data):
    Base = declarative_base()
    dburl = 'mysql+pymysql://python:python123@localhost:3308/testdb?charset=utf8mb4'
    engine = create_engine(dburl, encoding='utf-8')

    class Movie_table(Base):
        __tablename__ = f'movie_{movie_id}'
        id = Column(Integer(), primary_key=True, comment='主键ID')
        user = Column(String(50), comment='用户名')
        star = Column(SmallInteger(), comment='短评星级')
        ctime = Column(DateTime(), comment='短评时间')
        comment = Column(Text(), comment='短评内容')

        def __repr__(self):
            return f'{self.star} {self.ctime} {self.user} {self.comment}'

    # 创建表
    Base.metadata.create_all(engine)
    # 新建session
    dbsession = sessionmaker(bind=engine)
    session = dbsession()

    # 新增数据
    session.bulk_insert_mappings(Movie_table, data)
    try:
        session.commit()
        print(f'movie_id-{movie_id}: 数据保存完成')
    except Exception as err:
        raise Exception (f'movie_id-{movie_id}: 数据保存失败, {err}')

