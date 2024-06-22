#!/usr/bin/python3
"""
Script that lists all values in the `states` table of `hbtn_0e_0_usa`
where `name` matches the argument `state name searched`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name searched (str)
"""

import sys
import MySQLdb

def main():
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        return

    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]
    searched_name = sys.argv[4]

    try:
        # Establish a connection to the database
        db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name, host='localhost', port=3306)
        cur = db.cursor()

        # Execute the query to fetch states matching the searched name
        query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".format(searched_name)
        cur.execute(query)

        # Fetch all rows
        rows = cur.fetchall()

        # Print each row
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))

    finally:
        # Close cursor and connection
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    main()
