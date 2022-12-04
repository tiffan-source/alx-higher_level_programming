#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM `states`")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
