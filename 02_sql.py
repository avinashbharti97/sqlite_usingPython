import sqlite3

conn = sqlite3.connect("new.db")

c = conn.cursor()

cities = [('boston', 'MA', 6000),
          ('chicago', 'IL', 7000)]

c.executemany("INSERT INTO population VALUES(?, ?, ?)",cities)

conn.commit()
conn.close()