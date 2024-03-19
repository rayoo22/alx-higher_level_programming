#!/usr/bin/python3


""" script that lists all states from the database hbtn_0e_0_usa
takes 3 arguments mysql username, mysql password and database name
sorts results in ascending order by states.id
"""
import MySQLdb
import sys

try:
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    """ fetches results of the execution """
    list_of_states = cur.fetchall()

    for state in list_of_states:
        print(state)
    cur.close()
    db.close()

except MySQLdb.Error as e:
    print("Error:", e)
