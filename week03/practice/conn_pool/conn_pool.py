import pymysql
# 使用pip i
# pip install DBUtils 安装DBUtils
from dbutils.pooled_db import PooledDB
db_config = {
    "host": "localhost",
    "port": 3308,
    "user": "python",
    "passwd": "python123",
    "db": "testdb",
    "charset": "utf8mb4",
    "maxconnections": 0,        # 连接池允许的最大连接数
    "mincached": 4,             # 初始化连接池是至少创建的空闲连接
    "maxcached": 0,             # 连接池中最多闲置连接数，0位不限制
    "maxusage": 5,              # 每个连接最多被重用的次数，None为无限制
    "blocking": True            # 连接池中如果没有可用连接后是否阻塞等待，True等待，False不等待报错 
}

spool = PooledDB(pymysql, **db_config)

conn = spool.connection()
cursor = conn.cursor()
sql = "select version()"
cursor.execute(sql)
result = cursor.fetchall()
print(f"DB Version is {result}")

cursor.close()
conn.close()