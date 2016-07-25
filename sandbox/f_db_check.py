#!/usr/bin/python

import sqlite3
import os

#db_path = '~/git/meetme-selfservice/sandbox/mod.db'
db_path = './mod.db'
table = 'mod'


#os.system("file example.db")

conn = sqlite3.connect(db_path)

c = conn.cursor()

c.execute('CREATE TABLE if not exists ' + '"' + table + '"' + '(room_number, pin, creation_timestamp)')

conn.close()
