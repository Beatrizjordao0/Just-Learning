import os
'''
the codex - Youtube Class
18/04/2024
Python and MySQL - Query Conditions with WHERE and Wildcards
'''

import mysql.connector
# initialize the database
mydb = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", ""),
    database='testdb'
)

mycursor = mydb.cursor()

# sqlCommand = 'SELECT * FROM students WHERE name = "Sheila"'

                     # LIKE is something close to this ↓
sqlCommand = 'SELECT * FROM students WHERE name LIKE "%Th%" ' # we give it part of the name, and it returns for us
                                                             # names that looks like what we gave to it
                        
mycursor.execute(sqlCommand)

for age in mycursor:
    print(age)