# Agenda em Python usando Flask

Este projeto foi elaborado para permitir o aprendizado de conceitos como o padrão de projeto MVC (Model-View_Controller), framework Flask e seus componentes, variáveis de ambiente, paradigma de programação orientado a objetos e reforço de fundamentos da linguagem de programação Python.

Para implementar esse projeto localmente, siga os seguintes passos:

1. Faça um for deste repositório, clicando no botao `Fork`

2. Clone este repositório localmente:

~~~bash
git clone <url_seu_repositorio>
~~~

3. Abra o projeto utilizando seu IDE preferido

4. Crie, preferencialmente, um ambiente virtual utilizando sua versão do Python 
. >3.12.10

~~~bash
python -m venv .venv
~~~


5. Ative seu ambiente virtual.

    No bash: 

    ~~~bash
    source .venv/Scripts/activate
    ~~~

    No Powershell:

    ~~~powershell
    .\.venv\Scripts\Activate.ps1
    ~~~

    6. Instale todas as dependências constantes no `requirementes.txt`:

    ~~~python
    pip install -r requirements.txt
    ~~~

    7. Copie arquivo `.env.example`, cole na raiz do projeto e renomeie a 
    cópia para `.env`.

    8. Edite o arquivo `.env` para definir o caminho do seu banco de dados na constante `DATABASE`. Exemplo:

    ~~~env
    DATABASE='./data/meubanco.db'
    ~~~

    9. Rode a aplicação no Python utilizando o comando:

 ~~~bash
flask run
 ~~~

 10. Acesse a aplicação no endereço e porta indicados no terminal. Exemplo:
 `http://127.0.0.1:5000`