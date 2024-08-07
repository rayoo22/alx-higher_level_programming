#!/usr/bin/python3
""" listing all records in the states table """


if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    cur = db.cursor()

    statename = sys.argv[4]

    query = """
        SELECT * FROM states
        WHERE BINARY states.name = '{}'
        ORDER BY states.id ASC;
        """.format(statename)

    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
