from models.database import Database
from typing import Optional
from sqlite3 import Cursor
from datetime import datetime

class Tarefa:
    def __init__(self, titulo_tarefa: Optional[str], 
                 data_conclusao: Optional[str] = None, 
                 id_tarefa: Optional[int] = None, 
                 concluida: int = 0,
                 data_hora_conclusao: Optional[str] = None) -> None:
        self.titulo_tarefa = titulo_tarefa
        self.data_conclusao = data_conclusao
        self.id_tarefa = id_tarefa
        self.concluida = concluida
        self.data_hora_conclusao = data_hora_conclusao

    @classmethod
    def id(cls, id: int) -> "Tarefa":
        with Database() as db:
            query = 'SELECT titulo_tarefa, data_conclusao, concluida, data_hora_conclusao FROM tarefas WHERE id = ?;'
            params = (id,)
            resultado = db.buscar_tudo(query, params)
            [[titulo, data, concluida, data_hora]] = resultado
        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data, 
                   concluida=concluida, data_hora_conclusao=data_hora)

    def salvar_tarefa(self) -> None:
        with Database() as db:
            query = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
            params = (self.titulo_tarefa, self.data_conclusao)
            db.executar(query, params)

    @classmethod
    def obter_tarefas(cls) -> list["Tarefa"]:
        with Database() as db:
            query = 'SELECT titulo_tarefa, data_conclusao, id, concluida, data_hora_conclusao FROM tarefas;'
            resultados = db.buscar_tudo(query)
            return [cls(titulo, data, id, concluida, data_hora) for titulo, data, id, concluida, data_hora in resultados]

    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query = 'DELETE FROM tarefas WHERE id = ?;'
            params = (self.id_tarefa,)
            return db.executar(query, params)

    def atualizar_tarefa(self) -> Cursor:
        with Database() as db:
            query = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ? WHERE id = ?;'
            params = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            return db.executar(query, params)

    def concluir_tarefa(self) -> None:
        self.data_hora_conclusao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with Database() as db:
            query = "UPDATE tarefas SET concluida = 1, data_hora_conclusao = ? WHERE id = ?;"
            db.executar(query, (self.data_hora_conclusao, self.id_tarefa))
            self.concluida = 1

    def desmarcar_tarefa(self) -> None:
        with Database() as db:
            query = "UPDATE tarefas SET concluida = 0, data_hora_conclusao = NULL WHERE id = ?;"
            db.executar(query, (self.id_tarefa,))
            self.concluida = 0
            self.data_hora_conclusao = None