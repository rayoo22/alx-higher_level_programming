#!/usr/bin/python3
"""
a script displaying all values matching argument given
to do this, you separate the sql statement from the
argument given in the sql statement
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    #separate sql statement from the data given as argument
    #define the parameter value
    param = (sys.argv[4],)
    #define the sql query
    sql = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
    #execute statement
    cur.execute(sql, param)
    sim_list = cur.fetchall()

    for records in sim_list:
        print(records)

    cur.close()
    db.close()
