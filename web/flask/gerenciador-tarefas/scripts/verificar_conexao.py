import os
import mysql.connector

try:
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "GerenciadorDeTarefas")
    )
    print("Conexão bem-sucedida!")
except mysql.connector.Error as err:
    print("Erro ao conectar ao banco de dados:", err)
