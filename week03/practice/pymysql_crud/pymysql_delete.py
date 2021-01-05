import pymysql as db

HOST = 'localhost'
PORT = 3308
USER = 'python'
PASSWD = 'python123'
DBNAME = 'testdb'

conn = db.connect(HOST, USER, PASSWD, DBNAME, PORT)
try:
    with conn.cursor() as cursor:
        sql = 'DELETE FROM book where name=%s'
        value = ('百草园与三味书屋')
        cursor.execute(sql, value)
    conn.commit()
except Exception as err:
    print(f"Delete error {err}")
finally:
    conn.close()
    print(cursor.rowcount)
