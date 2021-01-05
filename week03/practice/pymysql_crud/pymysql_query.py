import pymysql as db

HOST = 'localhost'
PORT = 3308
USER = 'python'
PASSWD = 'python123'
DBNAME = 'testdb'

conn = db.connect(HOST, USER, PASSWD, DBNAME, PORT)

try:
    with conn.cursor() as cursor:
        sql = "SELECT id, name FROM book"
        cursor.execute(sql)
        books = cursor.fetchall()
        # print(books)
        # 返回元组，通过for循环取出
        for book in books:
            print(book)
    conn.commit()
except Exception as err:
    print(f"Insert error {err}")
finally:
    conn.close()
    print(cursor.rowcount)