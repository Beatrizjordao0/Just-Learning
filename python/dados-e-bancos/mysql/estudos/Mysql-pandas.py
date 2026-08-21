from pathlib import Path
import os
import mysql.connector
import pandas as pd
import numpy as np

df = pd.read_excel(Path(__file__).with_name("pokemon_data.xlsx"))

# initialize the database
mydb = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", ""),
    database='testdb'            # We use this to select the database we want to work with
)
# this is how python conects with mysql.
# this database cursor is like an input on command prompt
mycursor = mydb.cursor()

# print(df.columns)
# sqlCommand = (
#     "CREATE TABLE pokemon ("
#     "id INT(10), "
#     "name VARCHAR(255), "
#     "Type_1 VARCHAR(15), "
#     "Type_2 VARCHAR(15), "
#     "HP INT(20), "
#     "Attack INT(20), "
#     "Defense INT(20), "
#     "`Sp. Atk` INT(20), "
#     "`Sp. Def` INT(20), "
#     "Speed INT(20), "
#     "Generation INT(20), "
#     "Legendary VARCHAR(255)"
#     ")"
# )

# Substitua todos os valores NaN no DataFrame por None
# df = df.where(pd.notnull(df), None)

# for index, row in df.iterrows():
    
#     sql = (
#     "INSERT INTO pokemon (Name, Type_1, Type_2, HP, Attack, Defense, "
#     "`Sp. Atk`, `Sp. Def`, Speed, Generation, Legendary) "
#     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# )
#     values = (
        
#         row['Name'],
#         row['Type_1'],
#         row['Type_2'],
#         row['HP'],
#         row['Attack'],
#         row['Defense'],
#         row['Sp. Atk'],
#         row['Sp. Def'],
#         row['Speed'],
#         row['Generation'],
#         row['Legendary']
#     )
#     mycursor.execute(sql, values)
# mydb.commit()
# mycursor.close()

sql_add_column = "ALTER TABLE pokemon ADD COLUMN id INT PRIMARY KEY AUTO_INCREMENT"
mycursor.execute(sql_add_column)

update_sql = "UPDATE pokemon SET id = %s WHERE Name = %s"
for index, row in df.iterrows():
    values = (index + 1, row['Name'])  # Supondo que o índice comece em 0
    mycursor.execute(update_sql, values)

mydb.commit()