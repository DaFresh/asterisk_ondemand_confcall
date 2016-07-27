#!/usr/bin/python

import sqlite3
import os
import sys
import time
import datetime
from datetime import datetime, timedelta

# === VAR definition ===
db_path = '/Users/cedric_lemarchand/git/meetme-selfservice/sandbox/mod.db'
#table = ('mod')
time_now = datetime.now()
time_outdated = time_now - timedelta(hours=2)
room_range = range(100,105)

conn = sqlite3.connect(db_path)
c = conn.cursor()

time_minus_1h = time_now - timedelta(hours=1)
time_minus_2h = time_now - timedelta(hours=2)
time_minus_3h = time_now - timedelta(hours=3)
time_minus_4h = time_now - timedelta(hours=4)

test_datas = [('100', '123456', time_minus_1h),
                ('101', '123456', time_minus_2h),
                ('102', '123456', time_minus_3h),
                ('103', '123456', time_minus_4h),
                ]

# === Function definition ===
def drop_table():
        c.execute("DROP TABLE IF EXISTS mod")
        conn.commit
        return

def db_init():
        drop_table()
        c.execute("CREATE TABLE IF NOT EXISTS mod (room_number UNIQUE, pin, time_created DATE)" )
        c.executemany("INSERT INTO mod VALUES (?,?,?)", test_datas )
        conn.commit
        return

def print_all():
        #print "### DEBUG PRINT ALL"
        c.execute("SELECT * FROM mod")
        #print c.fetchall()
        for row in c:
                print row
        return


#db_init()
#print_all()

print "time_now = %s" % time_now
print "time_outdated = %s" % time_outdated
#time_diff = time_now - time_outdated
#print "NOW - OUTDATE %s" % time_diff
c.execute("DELETE FROM mod WHERE time_created > 'time_outdated' ")

conn.commit()

print "### AFTER DEL"
print_all()

sys.exit()

for i in room_range:
    print "### i = %s" % i
    c.execute("SELECT * FROM mod WHERE room_number = '%s' " % i )
    print c.fetchall()

# exception rides on duplicated key : sqlite3.IntegrityError: UNIQUE constraint failed: mod.room_number
conn.commit()
conn.close()
