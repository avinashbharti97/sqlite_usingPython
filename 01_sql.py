#Create a sqlite3 databse and table

#import the sqlite3 library
import sqlite3

#create a new database if the database doesn't exist
conn = sqlite3.connect("new.db")

#get the cursor object use to execute SQL command
c = conn.cursor()

#create a table
# c.execute("DROP TABLE population")
# c.execute("""CREATE TABLE population(city TEXT, state TEXT, population INTEGER)""")

#inserting data into table
c.execute("INSERT INTO population VALUES('Delhi', 'Mumbai', 9)")

#commit the changes
conn.commit()

#close the database connecton
conn.close()