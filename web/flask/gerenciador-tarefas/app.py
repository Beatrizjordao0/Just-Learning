import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Configurações do banco de dados
db_config = {
    'host': os.getenv("MYSQL_HOST", "localhost"),
    'user': os.getenv("MYSQL_USER", "root"),
    'password': os.getenv("MYSQL_PASSWORD", ""),
    'database': os.getenv("MYSQL_DATABASE", "GerenciadorDeTarefas")
}


# Página de Cadastro de Usuários
@app.route('/usuarios', methods=['GET'])
def show_users():
    return render_template('usuario.html')


# Rota para inserir um usuário
@app.route('/usuarios', methods=['POST'])
def create_user():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')

    if not all([nome, email]):
        return jsonify({"error": "Os campos nome e email são obrigatórios"}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO user (nome, email) VALUES (%s, %s)"
        cursor.execute(query, (nome, email))
        conn.commit()
        user_id = cursor.lastrowid
        return jsonify({"message": "Usuário cadastrado com sucesso!", "user_id": user_id}), 201

    except mysql.connector.Error as e:
        return jsonify({"error": f"Erro ao cadastrar usuário: {str(e)}"}), 500

    finally:
        cursor.close()
        conn.close()


# Página de Criação de Tarefas
@app.route('/tarefas', methods=['GET'])
def show_tasks():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Buscar todos os usuários do banco de dados
        cursor.execute("SELECT id, nome FROM user")
        users = cursor.fetchall()  # Retorna todos os usuários

        return render_template('tarefas.html', users=users)

    except mysql.connector.Error as e:
        return jsonify({"error": f"Erro ao buscar usuários: {str(e)}"}), 500

    finally:
        cursor.close()
        conn.close()


# Rota para inserir uma tarefa
@app.route('/tarefas', methods=['POST'])
def create_task():
    data = request.json
    descricao = data.get('descricao')
    setor = data.get('setor')
    prioridade = data.get('prioridade')
    status = data.get('status')
    user_id = data.get('user_id')

    if not all([descricao, setor, prioridade, status, user_id]):
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = """
        INSERT INTO tarefas (descricao, setor, prioridade, status, user_id) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (descricao, setor, prioridade, status, user_id))
        conn.commit()
        task_id = cursor.lastrowid
        return jsonify({"message": "Tarefa criada com sucesso!", "task_id": task_id}), 201

    except mysql.connector.Error as e:
        return jsonify({"error": f"Erro ao criar tarefa: {str(e)}"}), 500

    finally:
        cursor.close()
        conn.close()


# Página de Gerenciamento de Tarefas (mostrar as tarefas)
@app.route('/gerenciar', methods=['GET'])
def manage_tasks():
    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Consultar todas as tarefas no banco de dados
        cursor.execute("""
            SELECT t.id, t.descricao, t.setor, t.prioridade, t.status, u.nome
            FROM tarefas t
            JOIN user u ON t.user_id = u.id
        """)
        tasks = cursor.fetchall()  # Retorna todas as tarefas

        return render_template('gerenciar.html', tasks=tasks)  # Passa as tarefas para o template

    except mysql.connector.Error as e:
        return jsonify({"error": f"Erro ao buscar tarefas: {str(e)}"}), 500

    finally:
        cursor.close()
        conn.close()


# Rota padrão
@app.route('/')
def home():
    return render_template('usuario.html')


if __name__ == '__main__':
    app.run(debug=os.getenv("FLASK_DEBUG", "false").lower() == "true")
