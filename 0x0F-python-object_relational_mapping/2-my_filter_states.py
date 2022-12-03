#!/usr/bin/python3
"""2-filter_states module
contains a script that lists all states with a given name
from a given database
"""
from sys import argv

import MySQLdb


def list_all_states_filtered(username, password, db_name, state_name):
    """lists all states with the given name from a database

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

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
        .format(state_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    if (len(argv) - 1 >= 4):
        list_all_states_filtered(
            username=argv[1],
            password=argv[2],
            db_name=argv[3],
            state_name=argv[4]
        )
