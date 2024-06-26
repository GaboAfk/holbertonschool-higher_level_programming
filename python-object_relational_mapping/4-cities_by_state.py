#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=database
    )

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name\
               FROM cities\
                    JOIN states ON states.id = cities.state_id\
               ORDER BY cities.id")

    for state in c.fetchall():
        print(state)

    c.close()
    db.close()
