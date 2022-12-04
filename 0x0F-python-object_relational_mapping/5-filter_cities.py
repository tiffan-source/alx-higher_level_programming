#!/usr/bin/python3
""" script that takes in the name of a state as
an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    curs = db.cursor()
    query = """SELECT `cities`.`name`
        FROM `cities`
        LEFT JOIN `states`
        ON `cities`.`state_id` = `states`.`id`
        WHERE `states`.`name` = %s
        ORDER BY `cities`.`id`"""
    curs.execute(query, (sys.argv[4],))
    rows = curs.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    print(', '.join(result))
    curs.close()
    db.close()
