from sqlite3 import Connection, connect, Cursor
from types import TracebackType
from typing import Any, Self, Optional, Type
import traceback

class Database:
    def __init__(self, db_name: str) -> None:
        self.connection: Connection = connect(db_name)
        self.cursor: Cursor = self.connection.cursor()

    def executar(self, query: str, params: tuple = ()) -> Cursor:
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor
    
    def buscar_tudo(self, query: str, params: tuple = ()) -> list[Any]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def close(self) -> None:
        self.connection.close()

    
    # Métodos para o gerenciamento de contexto
    # Método de entrada no contexto
    def __enter__(self) -> Self:
        return self
    
    # Método de saída do contexto
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], tb: Optional[TracebackType]) -> None:
        
        if exc_type is not None:
            print('Exceção capturada no contexto:')
            print(f'Tipo: {exc_type.__name__}')
            print(f'Mensagem: {exc_value}')
            print('Traceback completo:')
            traceback.print_tb(tb)


        self.close()


# Área de Testes
# try:
#     db = Database('./data/tarefas.sqlite3')
#     db.executar('''
#     CREATE TABLE IF NOT EXISTS tarefas (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         titulo_tarefa TEXT NOT NULL,
#         data_conclusao TEXT);
#     ''')
#     db.executar('INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);', ('Estudar Python', '2026-02-02'))
# except Exception as e:
#     print(f"Erro ao criar a tabela: {e}")
# finally:
#     db.close()


