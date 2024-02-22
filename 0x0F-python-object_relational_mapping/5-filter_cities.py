#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities INNER JOIN states
                ON cities.state_id = (SELECT states.id
                WHERE states.name = %s)
                ORDER BY cities.id ASC""",
                (argv[4],))
    result = ''
    for row in cur:
        result += row[0] + ', '
    print(result.rstrip(', '))
