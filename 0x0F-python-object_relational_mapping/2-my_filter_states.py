#!/usr/bin/python3

"""
Displays all values in hbtn_0e_0_usa which match the argument
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    query = "SELECT * from states WHERE name = '{}';".format(sys.argv[4])
    cur.execute(query)
    states = cur.fetchall()

    for row in states:
        print(row)
