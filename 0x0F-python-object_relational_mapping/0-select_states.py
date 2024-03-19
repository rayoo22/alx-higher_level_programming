#!/usr/bin/python3


import MySQLdb
import sys
""" script that lists all states from the database hbtn_0e_0_usa
takes 3 arguments mysql username, mysql password and database name
sorts results in ascending order by states.id
"""

db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
cur = db.cursor()
lists_of_states = cur.execute("SELECT * FROM states ORDER BY states.id ASC")
print(list_of_states)
