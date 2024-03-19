#!/usr/bin/python3
"""
script taking in an argument and returns all values that
matches the argument given
"""


import MySQLdb
import sys

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
        # create cursor to execute queries using SQL
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY states.id".format(sys.argv[4]))
        # fetch results of execution
        sim_list = cur.fetchall()

        for records in sim_list:
            print(records)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error:", e)
