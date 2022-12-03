#!/usr/bin/python3
"""4-cities_by_state module
contains a script that lists all cities from a given database
"""
from sys import argv

import MySQLdb


def list_all_cities(username, password, db_name):
    """lists all cities from a database

    Args:
        username (str): mysql username
        password (str): mysql password
        db_name (str): the database name
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    if (len(argv) - 1 >= 3):
        list_all_cities(username=argv[1], password=argv[2], db_name=argv[3])
