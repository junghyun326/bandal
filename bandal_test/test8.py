# import requests #필수
import base64 #필수
import pymysql as sql
import pandas as pd

host_name = "bcc-database.cxmkpfyh3g9z.ap-northeast-2.rds.amazonaws.com"
username = "jeonghyun"
password = "bcc416416"
database_name = "bcc-database"

#연결된 db객체
conn = sql.connect(
    host = 'bcc-database.cxmkpfyh3g9z.ap-northeast-2.rds.amazonaws.com',
    user = 'jeonghyun',
    password = 'bcc416416',
    port = 3306,
    database = 'bcc-schema',
    charset='utf8')

# query = "SHOW TABLES"
# df = pd.read_sql(query, conn)
# print(df)

# query = "SELECT * FROM student"
# df = pd.read_sql(query, conn)
# print(df)

# cursor = conn.cursor()
# query = "insert into student (sid, sname, department) values (20169, '노르만디', '경영')"
# print(query)
# cursor.execute(query)
# conn.commit()
# print("record(s) inserted")

# cursor = conn.cursor()
# query = "delete from student where sid = 20169"
# print(query)
# cursor.execute(query)
# conn.commit()
# print("record(s) deleted")

cursor = conn.cursor()
query = "update student set sid = 20161 where sname = '유반달'"
print(query)
cursor.execute(query)
conn.commit()
print("record(s) updated")

# id = 20168
# query = "select * from student where sid = " + str(id)
# print(query)
# df = pd.read_sql(query, conn)
# print(df)



conn.close()