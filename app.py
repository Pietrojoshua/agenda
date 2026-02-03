from flask import Flask, render_template, request
from models.tarefa import Tarefa
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/agenda', methods=['GET','POST'])
def agenda():
    tarefas = None

    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()
        
    tarefas = Tarefa.obter_tarefas()   
    return render_template('agenda.html', titulo='Agenda', tarefas=tarefas)

@app.route('/delete/<int:idTarefa>')
def delete(idtarefa):
    tarefa = Tarefa.id(idtarefa)
    tarefa.excluir_tarefa()
    return



@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"
