#!/usr/bin/python3

""" A method that lists all states from the database hbtn_0e_0_usa. """
import sys
import MySQLdb


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=mysql_username,
                           passwd=mysql_password,
                           db=database_name,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
