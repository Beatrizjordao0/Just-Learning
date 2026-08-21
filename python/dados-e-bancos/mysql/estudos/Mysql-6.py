import os
'''
the codex - Youtube Class
18/04/2024
Python and MySQL - Ordering our Queries and Results
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

# This command will order every name by alphabetical order
sqlCommand = 'SELECT * FROM students ORDER BY name'

# This command line will order by ascending order
sqlCommand = 'SELECT * FROM students ORDER BY age'

# If I want descending order I add DESC
sqlCommand = 'SELECT * FROM students ORDER BY age DESC'

# DESC command also works for strings and VARCHAR like name
sqlCommand = 'SELECT * FROM students ORDER BY name DESC'

mycursor.execute(sqlCommand)

for name in mycursor:
    print(name)