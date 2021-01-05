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
        # 插入多条记录使用cursor.exceutemany()方法
        # value = (1005, '百年孤独')
        # cursor.execute(sql, value)
        values = ((1005, '百年孤独'),
                 (2011, 'Python爬虫最佳实践'),
                 (2012, 'ELK stack'),
                 (2013, 'Redis快速学习指南'),
                 )
        cursor.executemany(sql, values)
    conn.commit()
except Exception as err:
    print(f"数据库连接错误 {err}")
finally:
    conn.close()
    print(cursor.rowcount)
