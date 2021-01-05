import pymysql as db

HOST = 'localhost'
PORT = 3308
USER = 'python'
PASSWD = 'python123'
DBNAME = 'testdb'

conn = db.connect(HOST, USER, PASSWD, DBNAME, PORT)
try:
    with conn.cursor() as cursor:
        sql = "INSERT INTO book (id,name) VALUES (%s, %s)"
        # 插入多条记录使用cursor.executemany()方法
        value = (1006, '格林通话')
        cursor.execute(sql, value)
    conn.commit()
except Exception as err:
    print(f"数据库连接错误 {err}")
finally:
    conn.close()
    print(cursor.rowcount)
