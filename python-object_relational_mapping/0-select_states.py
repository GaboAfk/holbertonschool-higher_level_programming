#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username_ = argv[1]
    password_ = argv[2]
    database_ = argv[3]

db = MySQLdb.connect(
    host="localhost",#localhost está por default
    port=3306,#3306 está por defecto
    user=username_,
    password=password_,
    database=database_
)

c = db.cursor()
c.execute("SELECT * FROM states ORDER BY id")

[print(states) for states in c.fetchall()]

c.close()
db.close()
