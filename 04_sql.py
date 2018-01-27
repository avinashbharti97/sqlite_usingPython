import csv

import sqlite3

conn = sqlite3.connect("new.db")

c = conn.cursor()

c.execute("SELECT firstname, lastname FROM employees")

rows = c.fetchall()

for row in rows:
    print(row[0], row[1])

conn.commit()
conn.close()