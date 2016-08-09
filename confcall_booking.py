#!/usr/bin/python

import os
import sys
import time
import sqlite3
import datetime
from datetime import datetime, timedelta
from random import randrange

# === VAR definition ===
DEBUG = 0
#db_path = '/tmp/mod.db'
db_path = '/tmp/mod.db'
time_now = datetime.now()
time_outdated = time_now - timedelta(seconds=1) # room's timeout settings
room_range = range(100,105) # use db_init() after changing this value
random_pin = randrange(100000,999999) # rooms's range settings, to be improved with rstr module

conn = sqlite3.connect(db_path)
c = conn.cursor()

# === FUNC definition ===
def db_drop():
    "Drop the db 'mod'"
    c.execute("DROP TABLE IF EXISTS mod")
    conn.commit
    return

def db_init():
    "Create/re-create the db 'mod' and table 'mod'"
    c.execute("CREATE TABLE IF NOT EXISTS mod (room_number UNIQUE, pin, time_created DATE)" )

def db_init_test_datas():
    "Put some data for testing purpose"
    time_minus_1h = time_now - timedelta(hours=1)
    time_minus_2h = time_now - timedelta(hours=2)
    time_minus_3h = time_now - timedelta(hours=3)
    time_minus_4h = time_now - timedelta(hours=4)

    test_datas = [('100', '123456', time_minus_1h),
                    ('101', '123456', time_minus_2h),
                    ('102', '123456', time_minus_3h),
                    ('103', '123456', time_minus_4h),
                    ]
    c.executemany("INSERT INTO mod VALUES (?,?,?)", test_datas )
    conn.commit()
    return

def db_print_all():
    "Print all db content"
    print "### DEBUG PRINT ALL:"
    c.execute("SELECT * FROM mod")
    for row in c:
        print row
    return

def db_clean():
    "Remove oudated entry, cf 'time_outdated' variable "
    c.execute("SELECT * FROM mod WHERE time_created < '%s' " % time_outdated )
    if DEBUG: print "### Deleted outdated row : %s" % c.fetchall()
    c.execute("DELETE FROM mod WHERE time_created < '%s' " % time_outdated )
    conn.commit()

def db_find_free_room():
    for i in room_range:
        if DEBUG : print "### i = ", i
        try:
            new_room = (i, random_pin, time_now)
            c.execute("INSERT INTO mod VALUES (?,?,?)", new_room )
            print 'SET VARIABLE STATUS "OK"'
            print 'SET VARIABLE ROOM_NUMBER "%s"' % i
            print 'SET VARIABLE ROOM_PIN "%s"' % random_pin
            print i, random_pin
            if DEBUG: print "### New room created with : ", new_room
            conn.commit()
            break
        except sqlite3.IntegrityError:
            if DEBUG : print "### IntegrityError, table %s exist" % i
    else:
        print 'SET VARIABLE STATUS "FULL"'
        if DEBUG : print "### No more available room"

def db_check_pin():
    "Find related pin"
    if DEBUG : print "Looking for pin of room %s" % room_number
    #c.execute("SELECT pin FROM mod WHERE room_number = '%s'" % room_number)
    cursor = c.execute("SELECT pin FROM mod WHERE room_number= %s " % room_number)
    #print cursor.in_transaction
    #print sqlite3.complete_statement("SELECT pin FROM mod WHERE room_number= %s " % room_number)
    data = cursor.fetchall()

    if (len(data) == 0):
        print 'SET VARIABLE STATUS "NOK"'
        if DEBUG: print "No pin found for room %s, seems room did not exist" % room_number
    elif (len(data) == 1):
        for row in data:
            if row:
                room_pin = str(row[0])
                if DEBUG: print "room_pin = %s, user_pin = %s" % (room_pin, user_pin)
                if (room_pin == user_pin): print 'SET VARIABLE STATUS "OK"'
                if (room_pin != user_pin): print 'SET VARIABLE STATUS "NOK"'
    else:
            if DEBUG: print "Error"
            print 'SET VARIABLE STATUS "OK"'

if DEBUG: db_print_all()

# === Booking mode ===
if len(sys.argv) == 1:
    db_init()
    db_clean()
    db_find_free_room()
    conn.close()
    #sys.exit(0)

# === Checking mode ===
elif len(sys.argv) == 3:
    room_number = str(sys.argv[1])
    user_pin = str(sys.argv[2])
    db_clean()
    db_check_pin()
    conn.close()
    #sys.exit(0)
else:
    print "Error, unsupported usage"
    sys.exit(2)

#db_drop()
#db_init()
#db_clean()
#db_find_free_room()
#conn.commit()
#conn.close()
