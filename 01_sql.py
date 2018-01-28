#Create a sqlite3 databse and table

#import the sqlite3 library
import sqlite3

#create a new database if the database doesn't exist
conn = sqlite3.connect("new.db")

#get the cursor object use to execute SQL command
c = conn.cursor()


cities	=	[
                ('Boston',	'MA',	600000),
			    ('Los	Angeles',	'CA',	38000000),
				('Houston',	'TX',	2100000),
				('Philadelphia',	'PA',	1500000),
				('San	Antonio',	'TX',	1400000),
				('San	Diego',	'CA',	130000),
				('Dallas',	'TX',	1200000),
				('San	Jose',	'CA',	900000),
				('Jacksonville',	'FL',	800000),
				('Indianapolis',	'IN',	800000),
			    ('Austin',	'TX',	800000),
				('Detroit',	'MI',	700000)
			]
#create a table
# c.execute("DROP TABLE population")
# c.execute("""CREATE TABLE population(city TEXT, state TEXT, population INTEGER)""")

#inserting data into table
c.executemany("INSERT INTO population VALUES(?, ?, ?)",cities)

#commit the changes
conn.commit()

#close the database connecton
conn.close()