#!/usr/bin/python3
""" script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    curs = db.cursor()
    query = "SELECT * FROM `states`\
        WHERE `states`.`name` = '{:s}'\
        ORDER BY `states`.`id`".format(sys.argv[4])
    curs.execute(query)
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
