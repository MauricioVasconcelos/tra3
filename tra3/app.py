from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='db',
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD']
    )
    return conn

@app.route('/')
def index():
    return "Bem-vindo à aplicação de gestão de tarefas!"

@app.route('/usuarios')
def get_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM usuarios;')
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(usuarios)

@app.route('/tarefas')
def get_tarefas():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM tarefas;')
    tarefas = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(tarefas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

