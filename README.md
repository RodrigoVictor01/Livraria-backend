# Projeto com Python, Django e PostgreSQL


## Requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [pip](https://pip.pypa.io/en/stable/)

## Instalação

1. **Clone o repositório e vá até o diretório:**

    ```bash
    git clone https://github.com/RodrigoVictor01/Livraria-backend.git
    cd livraria-backend
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**

    Está presente o arquivo `requirements.txt` no diretório do projeto. Instale as dependências com:

    ```bash
    pip install -r requirements.txt
    ```
    
    3.1 Como usar o `.env.example`:

    No diretório raiz do projeto, você encontrará o arquivo `.env.example`.
    Crie uma cópia desse arquivo e renomeie para `.env`:
   ```bash
   cp .env.example .env
   ```
    

4. **Configure o banco de dados PostgreSQL:**

    1. **Crie um banco de dados PostgreSQL:**

        Acesse o terminal do PostgreSQL:

        ```bash
        psql -U seu_usuario
        ```

        No terminal do PostgreSQL, crie um banco de dados:

        ```sql
        CREATE DATABASE livraria_db;
        ```

        Saia do `psql`:

        ```sql
        \q
        ```

    2. **Configure as credenciais do banco de dados:**

        No arquivo de configuração do seu projeto (por exemplo, `settings.py` para Django ou um arquivo de configuração específico), adicione as credenciais do banco de dados:

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'livraria_db',
                'USER': 'seu_usuario',
                'PASSWORD': 'sua_senha',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
        ```

        Substitua `seu_usuario` e `sua_senha`.

5. **Aplique as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

6. **Execute o projeto:**

    ```bash
    python manage.py runserver
    ```


## Contato

Se tiver alguma dúvida ou precisar de ajuda adicional, entre em contato com [rodrigo.victor.3344@live.com](mailto:rodrigo.victor.3344@live.com).

    

