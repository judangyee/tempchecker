import pymysql
import pandas as pd
import datetime

connect = pymysql.connect(host='localhost', user='root', password='songjy(05)', db='seongbok',\
                          charset='utf8mb4')
cur = connect.cursor()


query = "SELECT * FROM student"
cur.execute(query)
connect.commit()

datas = cur.fetchall()
for data in datas:
    print(data)

