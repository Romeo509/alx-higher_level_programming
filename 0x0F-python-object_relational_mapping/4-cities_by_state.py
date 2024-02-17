#!/usr/bin/python3
"""
Script that list all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()

    query = """
             SELECT cities.id, cities.name, states.name
             FROM cities
             JOIN states ON cities.state_id = states.id
             ORDER BY cities.id
             """
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
