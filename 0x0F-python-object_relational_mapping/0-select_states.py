#!/usr/bin/python3
from sys import argv

import MySQLdb


def list_all_states(username, password, db_name):
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    if (len(argv) - 1 >= 3):
        list_all_states(username=argv[1], password=argv[2], db_name=argv[3])
