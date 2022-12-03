#!/usr/bin/python3
"""5-filter_cities module
contains a script that lists all cities of a given state
from a given database and is sql-injection safe
"""
from sys import argv

import MySQLdb


def list_all_cities_filtered(username, password, db_name, state_name):
    """lists all cities of a given state

    Args:
        username (str): mysql username
        password (str): mysql password
        db_name (str): the database name
        state_name (str): the state name
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
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, [state_name])
    query_rows = cur.fetchall()
    print(*[row[0] for row in query_rows], sep=', ')

    cur.close()
    conn.close()


if __name__ == "__main__":
    if (len(argv) - 1 >= 4):
        list_all_cities_filtered(
            username=argv[1],
            password=argv[2],
            db_name=argv[3],
            state_name=argv[4]
        )
