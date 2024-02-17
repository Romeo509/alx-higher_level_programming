#!/usr/bin/python3
"""
Lists all cities of a given state from the database
hbtn_0e_4_usa (SQL injection free).
"""

import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
    """
    Connects to the MySQL server and displays cities of
    the given state (SQL injection free).

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

        query = """SELECT cities.name
                   FROM cities
                   INNER JOIN states ON states.id = cities.state_id
                   WHERE states.name = %s"""
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()
        city_names = [row[0] for row in rows]
        print(", ".join(city_names))

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
        print("""Usage: {} <username> <password> <database>
              <state_name>""".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities(username, password, database, state_name)
