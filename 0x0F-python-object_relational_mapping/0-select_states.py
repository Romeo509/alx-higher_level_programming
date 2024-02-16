#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters from command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
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

        # Execute SQL query to retrieve and display states
        cursor.execute("SELECT * FROM states ORDER BY id ASC;")
        states = cursor.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        # Close the database connection
        if db:
            db.close()
