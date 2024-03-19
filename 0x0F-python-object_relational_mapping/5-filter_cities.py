#!/usr/bin/python3
"""
script takes in the name of a state as an arg
and lists all cities of that state
the script should be SQL injection free
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # creating connection
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # create cursor to enable execution of sql statements
    cur = db.cursor()
    # script preventing sql injection
    param = (sys.argv[4],)
    # sql statement
    sql = "SELECT cities.name FROM cities WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name=%s) ORDER BY cities.id ASC"
    cur.execute(sql, param)
    # fetch results of the execution above
    cities_list = cur.fetchall()

    for city in cities_list:
        print(city)
