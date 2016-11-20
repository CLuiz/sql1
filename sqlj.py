# SQLite Functions

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    # create a dict of sql queries
    sql = {'average': 'SELECT AVG(population) FROM population',
           'maximum': 'SELECT MAX(population) FROM population',
           'minimum': 'SELECT MIN(population) FROM population',
           'sum': 'SELECT SUM(population) FROM population',
           'count': 'SELECT COUNT(population) FROM population'}

    # run each sql query item in the dictionary:
    for k, v in sql.iteritems():

        # run sql
        c.execute(v)

        # fetchone() retrieves one record from query
        result = c.fetchone()

        # output the result to screen
        print k + ': ', result[0]
