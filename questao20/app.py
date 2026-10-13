from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

BANCO = "tarefas.db"


# Classe que representa uma tarefa.
# Ela guarda o título e se a tarefa foi concluída.
class Tarefa:
    def __init__(self, titulo, concluida=False):
        self.titulo = titulo
        self.concluida = concluida


# Abre a conexão com o banco de dados.
def conectar():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


# Cria a tabela caso ela ainda não exista.
def criar_tabela():
    with conectar() as banco:
        banco.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                concluida INTEGER NOT NULL DEFAULT 0
            )
        """)


# GET: busca as tarefas no banco e mostra na página.
@app.route("/")
def inicio():
    with conectar() as banco:
        registros = banco.execute(
            "SELECT * FROM tarefas ORDER BY id DESC"
        ).fetchall()

    # A lista guarda as tarefas encontradas no banco.
    tarefas = [
        Tarefa(registro["titulo"], bool(registro["concluida"]))
        for registro in registros
    ]

    return render_template(
        "index.html",
        tarefas=registros,
        objetos_tarefa=tarefas
    )


# CREATE: cadastra uma nova tarefa no banco.
@app.route("/criar", methods=["POST"])
def criar():
    titulo = request.form.get("titulo", "").strip()

    # Verifica se o título não está vazio.
    if titulo:
        tarefa = Tarefa(titulo)

        with conectar() as banco:
            banco.execute(
                "INSERT INTO tarefas (titulo, concluida) VALUES (?, ?)",
                (tarefa.titulo, int(tarefa.concluida))
            )

    return redirect(url_for("inicio"))


# UPDATE: altera o título de uma tarefa existente.
@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    titulo = request.form.get("titulo", "").strip()

    # Só altera se o título não estiver vazio.
    if titulo:
        with conectar() as banco:
            banco.execute(
                "UPDATE tarefas SET titulo = ? WHERE id = ?",
                (titulo, id)
            )

    return redirect(url_for("inicio"))


# DELETE: exclui uma tarefa pelo seu ID.
@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    with conectar() as banco:
        banco.execute(
            "DELETE FROM tarefas WHERE id = ?",
            (id,)
        )

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    criar_tabela()  # Garante que a tabela exista.
    app.run(debug=True)  # Inicia o servidor local.

# CLIENTE-SERVIDOR:
# O cliente é o navegador, onde o usuário acessa a página.
# O servidor é o Flask, que recebe e processa as requisições.
# O SQLite armazena as tarefas cadastradas.

# A lista armazena as tarefas consultadas no banco.
# Uma lista permite guardar vários elementos em uma única estrutura.

# A classe Tarefa representa uma tarefa.
# Seus atributos são titulo e concluida.
# Cada objeto criado a partir dela representa uma tarefa.

# GET: consulta e mostra as tarefas.
# POST: envia dados para cadastrar, alterar ou excluir tarefas.