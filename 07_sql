import sqlite3

conn = sqlite3.connect("new.db")

c  = conn.cursor()

c.execute("""SELECT DISTINCT population.city, population.population, regions.region FROM population, regions WHERE population.city = regions.city ORDER BY population.city ASC """)
conn.commit()
conn.close()