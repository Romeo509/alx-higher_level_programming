#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


def list_states(username, password, database):
    """Connects to the MySQL server and lists states starting with 'N'
       from the specified database."""
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cur = db.cursor()

        cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                    ORDER BY id;""")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    """Main script execution block."""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    list_states(username, password, database)
