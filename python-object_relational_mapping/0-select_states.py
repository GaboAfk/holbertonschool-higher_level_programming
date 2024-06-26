#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username_ = argv[1]
    password_ = argv[2]
    database_ = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username_,
        password=password_,
        database=database_
    )

    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")

    for state in c.fetchall():
        print(state)

    c.close()
    db.close()
