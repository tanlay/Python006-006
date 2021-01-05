import pymysql as db

HOST = 'localhost'
PORT = 3308
USER = 'python'
PASSWD = 'python123'
DBNAME = 'testdb'

conn = db.connect(HOST, USER, PASSWD, DBNAME, PORT)
try:
    with conn.cursor() as cursor:
        sql = "select version()"
        # 使用execute方法执行SQL
        cursor.execute(sql)
        result = cursor.fetchone()
    conn.commit()
except Exception as err:
    print(f"数据库连接失败")
finally:
    # 关闭数据库连接
    conn.close()

print(f"DB version: {result}")
