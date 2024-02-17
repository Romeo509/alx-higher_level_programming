#!/usr/bin/python3
import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Connects to a MySQL server and lists states with names starting
     with 'N' from the specified database.
    :param username: MySQL username
    :param password: MySQL password
    :param database: Database name
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'"
                       " ORDER BY id ASC;")
        states = cursor.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    """
    Main script execution block.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    filter_states(username, password, database)
