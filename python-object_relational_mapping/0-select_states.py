#!/usr/bin/python3
"""
Script that lists all `states` from the database `hbtn_0e_0_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
import MySQLdb

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        return

    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Establish a connection to the database
        db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name)
        cur = db.cursor()

        # Execute the query to fetch all states ordered by id
        cur.execute("SELECT * FROM states ORDER BY id")
        rows = cur.fetchall()

        # Print each row
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))

    finally:
        # Close cursor and connection
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    main()
