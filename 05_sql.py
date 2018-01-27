import sqlite3

conn = sqlite3.connect("new.db")
c = conn.cursor()

c.execute("UPDATE employees SET firstname = 'avinash' WHERE lastname = 'Bird'")
c.execute("DELETE FROM employees WHERE lastname = 'Blake'")

c.execute("SELECT * FROM employees")
rows = c.fetchall()

for row in rows:
    print(row[0], row[1])

conn.commit()
conn.close()