# Create a SQLite3 database and table

# import SQLite3
import sqlite3

# create a database if the database doesn't already exist
conn = sqlite3.connect('new.db')

# instantiate a cursor object
cursor = conn.cursor()

# create a table
cursor.execute('''CREATE TABLE population
                (city TEXT, state TEXT, population INT)''')

# close the connection
conn.close()
