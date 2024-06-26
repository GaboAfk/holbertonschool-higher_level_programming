#!/usr/bin/python3
"""write a script that takes in arguments and
   displays all values in the states table of
   hbtn_0e_0_usa where name matches the argument.
   But this time, write one that is safe from
   MySQL injections!"""
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
               WHERE BINARY name = %s\
               ORDER BY id", (state_name,))

    for state in c.fetchall():
        print(state)

    c.close()
    db.close()
