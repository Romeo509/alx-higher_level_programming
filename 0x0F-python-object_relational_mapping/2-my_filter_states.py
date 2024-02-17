#!/usr/bin/python3
"""
Displays all values in the states table of
hbtn_0e_0_usa where the name matches the provided argument.
"""

import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    Connects to the MySQL server and displays states with names
     matching the provided argument.

    :param username: MySQL username
    :param password: MySQL password
    :param database: Database name
    :param state_name: State name to search for
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    """
    Main script execution block.
    """
    if len(sys.argv) != 5:
        print("""Usage: {} <username> <password>
              <database> <state_name>""".format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_states(username, password, database, state_name)
