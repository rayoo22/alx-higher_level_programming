#!/usr/bin/python3
"""
lists all stats with name starting with 'N'
results must be sorted in ascending order
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    """lists states starting with 'N'"""
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    """fetches results of execution above"""
    n_states = cur.fetchall()

    for n in n_states:
        print(n)
    cur.close()
    db.close()
