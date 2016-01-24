print ("************" * 1)
print ("Connect to SQL database")
print ("************\n" * 1)

import sqlite3

sqlite_file = 'C:\sqlite\company.db' ## the database file

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT * from employee where empid>102')
all_rows = c.fetchall()
c.execute('SELECT * from employee where empid>102')
row = c.fetchone()
while row is not None:
    print(row)
    row = c.fetchone()

conn.close()
