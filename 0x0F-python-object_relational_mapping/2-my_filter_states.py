#!/usr/bin/python3

"""
Displays all values in hbtn_0e_0_usa
which match the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * \
            FROM states \
            WHERE name = '{}';".format(sys.argv[4]))
    states = cur.fetchall()

    for state in states:
        print(state)
