#!/usr/bin/python3


"""Prints records for a given state"""


import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                    WHERE LIKE BINARY '{}'\
                    ORDER BY id ASC".format(sys.argv[4]))
    res = cursor.fetchall()

    for rec in res:
        print(rec)

    cursor.close()
    db.close()
