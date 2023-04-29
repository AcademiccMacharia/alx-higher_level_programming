#!/usr/bin/python3
"""
Lists all the states
"""

import sys
import MySQLdb

if __name__ = '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * from states;")
    states = cur.fetchall()

    for i in states:
        print(i)
