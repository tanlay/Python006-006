import pymysql as db
from dbconfig import read_db_config

dbsrv = read_db_config()
conn = db.connect(**dbsrv)

try:
    with conn.cursor() as cursor:
        sql = 'SELECT VERSION()'
        cursor.execute(sql)
        result = cursor.fetchone()
    conn.commit()
except Exception as err:
    print(f"数据库连接错误 {err}")
finally:
    conn.close()

print(f"DB Version is: {result}")
