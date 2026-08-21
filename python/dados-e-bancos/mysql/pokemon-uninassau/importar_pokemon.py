from pathlib import Path
import os
import mysql.connector
import pandas as pd
import ast, json

# Conecta no MySQL
mydb = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="pokemons"
)
cursor = mydb.cursor()

# Lê o CSV
df = pd.read_csv(Path(__file__).with_name("pokemon.csv"), encoding="utf-8")

# Colunas do MySQL
colunas_mysql = [
    'abilities','against_bug','against_dark','against_dragon','against_electric','against_fairy',
    'against_fight','against_fire','against_flying','against_ghost','against_grass','against_ground',
    'against_ice','against_normal','against_poison','against_psychic','against_rock','against_steel',
    'against_water','attack','base_egg_steps','base_happiness','base_total','capture_rate','classfication',
    'defense','experience_growth','height_m','hp','japanese_name','name','percentage_male','pokedex_number',
    'sp_attack','sp_defense','speed','type1','type2','weight_kg','generation','is_legendary'
]

# Converte abilities para JSON
df['abilities'] = df['abilities'].apply(lambda x: json.dumps(ast.literal_eval(x)) if pd.notnull(x) else '[]')

# Substitui NaN por None
df = df.where(pd.notnull(df), None)

# Gera lista de tuplas
valores = [tuple(x) for x in df[colunas_mysql].astype(object).to_numpy()]

# Monta SQL
sql = f"INSERT INTO pokemonsinfo ({', '.join(colunas_mysql)}) VALUES ({', '.join(['%s']*len(colunas_mysql))})"

# Executa
cursor.executemany(sql, valores)
mydb.commit()
cursor.close()
mydb.close()

print("Todos os dados inseridos com sucesso!")
