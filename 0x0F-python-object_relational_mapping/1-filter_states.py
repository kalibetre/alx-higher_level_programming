#!/usr/bin/python3
"""1-filter_states module
contains a script that lists all states with a name starting
with N from a given database
"""
from sys import argv

import MySQLdb


def list_all_states_filtered(username, password, db_name):
    """lists all states with a name that starts with N from a database

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
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    if (len(argv) - 1 >= 3):
        list_all_states_filtered(
            username=argv[1], password=argv[2], db_name=argv[3])
