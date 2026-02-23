from flask import Flask, render_template, request, redirect, url_for
from models.tarefa import Tarefa
from models.database import init_db

app = Flask(__name__)
init_db()  # Inicializa o banco e garante que todas as colunas existam

# ----------------- Home -----------------
@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

# ----------------- Agenda -----------------
@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao'] or None
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()
        return redirect(url_for('agenda'))

    tarefas = Tarefa.obter_tarefas()
    return render_template('agenda.html', titulo='Agenda', tarefas=tarefas, tarefa_selecionada=None)

# ----------------- Atualizar tarefa -----------------
@app.route('/update/<int:idTarefa>', methods=['GET', 'POST'])
def update(idTarefa):
    tarefa_selecionada = Tarefa.id(idTarefa)
    if request.method == 'POST':
        titulo = request.form['titulo-tarefa']
        data = request.form['data-conclusao'] or None
        tarefa = Tarefa(titulo, data, idTarefa)
        tarefa.atualizar_tarefa()
        return redirect(url_for('agenda'))

    tarefas = Tarefa.obter_tarefas()
    return render_template('agenda.html', titulo=f'Editando a tarefa ID: {idTarefa}',
                           tarefas=tarefas, tarefa_selecionada=tarefa_selecionada)

# ----------------- Excluir tarefa -----------------
@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    if not tarefa.concluida:  # Não apaga tarefas concluídas
        tarefa.excluir_tarefa()
    return redirect(url_for('agenda'))

# ----------------- Concluir tarefa -----------------
@app.route('/concluir/<int:idTarefa>')
def concluir(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.concluir_tarefa()
    return redirect(url_for('agenda'))

# ----------------- Desmarcar tarefa -----------------
@app.route('/desmarcar/<int:idTarefa>')
def desmarcar(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.desmarcar_tarefa()
    return redirect(url_for('agenda'))

if __name__ == "__main__":
    app.run(debug=True)