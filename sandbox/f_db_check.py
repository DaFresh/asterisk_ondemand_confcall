#!/usr/bin/python

import sqlite3
import os
import time
import datetime

#db_path = '~/git/meetme-selfservice/sandbox/mod.db'
db_path = '/Users/cedric_lemarchand/git/meetme-selfservice/sandbox/mod.db'
table = ('mod')

range = ('100','200')

#os.system("file example.db")

conn = sqlite3.connect(db_path)
c = conn.cursor()

time_now = (int(time.time()))

test_data = [('100', '123456', time_now),
                ('101', '123456', time_now),
                ('102', '123456', time_now),
                ('103', '123456', time_now),
                ]

c.execute("DROP TABLE '%s'" % table)

c.execute("CREATE TABLE IF NOT EXISTS '%s' (room_number, pin, age INTERGER)" % table)

c.executemany("INSERT INTO '%s' VALUES (?,?,?)" % table, test_data)

c.execute("CREATE TABLE IF NOT EXISTS '%s' (room_number, pin, creation_timestamp)" % table)


c.execute("SELECT * FROM '%s' " % table)

#c.execute("DELETE FROM  mod WHERE room_number < "101")

for row in c:
        print row

conn.commit()
conn.close()
