#!/usr/bin/env python

import random,pymysql

db = pymysql.connect("localhost", "root", "", "showmethecode")

cursor = db.cursor()

n = 1
while n <= 200:
    sql = "Insert INTO 0002PromoCode (promocode, isused) values('" + "".join(random.choices("ABCDEFGHJKMNPQRSTUVWXY1234567890",k=10)) + "', '0')"
    cursor.execute(sql)
    n += 1

db.commit()
db.close()