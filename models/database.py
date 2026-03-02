from sqlite3 import Connection, connect, Cursor
from types import TracebackType
from typing import Any, Optional, Type
import traceback
import os
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv('DATABASE', './data/tarefas.sqlite3')

def init_db(db_name: str = DB_PATH) -> None:
    
    data_dir = os.path.join(os.getcwd(), "data")

    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)

    with connect(db_name) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo_tarefa TEXT NOT NULL,
            data_conclusao TEXT
        );
        ''')
        
        cursor.execute("PRAGMA table_info(tarefas);")
        colunas = [info[1] for info in cursor.fetchall()]
        
        if 'concluida' not in colunas:
            cursor.execute("ALTER TABLE tarefas ADD COLUMN concluida" 
            " INTEGER DEFAULT 0;")
        
        if 'data_hora_conclusao' not in colunas:
            cursor.execute("ALTER TABLE tarefas ADD COLUMN data_hora_conclusao" 
            " TEXT;")
        conn.commit()

class Database:
    """Classe para gerenciar conexões e operações com SQLite usando contexto"""

    def __init__(self, db_name: str = DB_PATH) -> None:
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

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 tb: Optional[TracebackType]) -> None:
        if exc_type:
            print('Exceção capturada no contexto:')
            print(f'Tipo: {exc_type.__name__}')
            print(f'Mensagem: {exc_value}')
            print('Traceback completo:')
            traceback.print_tb(tb)
        self.close()