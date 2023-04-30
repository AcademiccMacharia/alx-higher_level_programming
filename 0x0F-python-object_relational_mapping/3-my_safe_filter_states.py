#!/usr/bin/python3

"""
List all values that match the argument safely
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name = %s;", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)
