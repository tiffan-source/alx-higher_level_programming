#!/usr/bin/python3
""" script that lists all cities
from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    curs = db.cursor()
    query = """SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
        FROM `cities`\
        LEFT JOIN `states`\
        ON `cities`.`state_id` = `states`.`id`\
        ORDER BY `cities`.`id`"""
    curs.execute(query)
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
