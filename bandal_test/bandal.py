import pymysql as sql

conn = sql.connect(
    host = 'bcc-database.cxmkpfyh3g9z.ap-northeast-2.rds.amazonaws.com',
    user = 'jeonghyun',
    password = 'bcc416416',
    port = 3306,
    database = 'bcc-schema',
    charset='utf8')

cursor = conn.cursor()

query = "update student set sid = 20161 where sname = '유반달'"
cursor.execute(query)
conn.commit()

conn.close()