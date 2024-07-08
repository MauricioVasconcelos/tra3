-- Criação do banco de dados e tabelas

CREATE DATABASE gestao_tarefas;

\connect gestao_tarefas;

-- Criação da tabela usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);

-- Criação da tabela tarefas
CREATE TABLE tarefas (
    id SERIAL PRIMARY KEY,
    descricao TEXT NOT NULL,
    status TEXT NOT NULL,
    usuario_id INTEGER REFERENCES usuarios(id)
);

-- Inserção de dados fictícios

-- Usuários
INSERT INTO usuarios (nome, email, senha) VALUES
('Alice', 'alice@example.com', 'senha1'),
('Bob', 'bob@example.com', 'senha2'),
('Carol', 'carol@example.com', 'senha3');

-- Tarefas
INSERT INTO tarefas (descricao, status, usuario_id) VALUES
('Tarefa 1', 'pendente', 1),
('Tarefa 2', 'concluída', 1),
('Tarefa 3', 'pendente', 2),
('Tarefa 4', 'concluída', 3);
