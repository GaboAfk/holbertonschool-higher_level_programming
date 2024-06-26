#!/usr/bin/python3
"""takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa where
   name matches the argument."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=database
    )

    c = db.cursor()
    c.execute("SELECT * FROM states\
               WHERE BINARY name = '{}'\
               ORDER BY id".format(state_name))

    for state in c.fetchall():
        print(state)

    c.close()
    db.close()
