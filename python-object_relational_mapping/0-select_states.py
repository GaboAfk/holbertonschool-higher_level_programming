#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
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
c.execute("SELECT * FROM states ORDER BY id")

for state in c.fetchall():
    print(state)

c.close()
db.close()
