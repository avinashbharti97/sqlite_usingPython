#import csv file
import csv

#import sqlite3
import sqlite3

#make connection
conn = sqlite3.connect("new.db")

#make cursor
c = conn.cursor()

#opening csv file present in directory
employees = csv.reader(open("employees.csv", "rU"))



#create a new table named employees
c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

#insert data into table
c.executemany("INSERT INTO employees(firstname, lastname) VALUES(?, ?)", employees)

conn.commit()
conn.close()
