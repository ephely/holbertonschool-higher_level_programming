#!/usr/bin/python3
"""
Wait, do you remember the previous task? Did you test "Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Verification of all required arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name>\
              <state name searched>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Command line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connection to MySQL Server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Creating Cursor
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close
