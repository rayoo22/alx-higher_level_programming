#!/usr/bin/python3
"""
script listing all cities from database
using execute() once
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # create cursor for executing sql statement
    cur = db.cursor()
    # sql statement
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    # fetch results of the executed sql statement
    cities = cur.fetchall()

    for city in cities:
        print(cities)

    cur.close()
    db.close()
