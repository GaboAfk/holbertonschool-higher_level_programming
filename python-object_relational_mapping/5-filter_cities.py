#!/usr/bin/python3
"""takes in the name of a state as an argument
   and lists all cities of that state, using
   the database hbtn_0e_4_usa"""
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
    c.execute("SELECT cities.name\
               FROM cities\
                    JOIN states ON states.id = cities.state_id\
               WHERE BINARY states.name = %s\
               ORDER BY cities.id", (state_name, ))

    print(", ".join([states[0] for states in c.fetchall()]))

    c.close()
    db.close()
