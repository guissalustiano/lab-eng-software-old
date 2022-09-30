# lab-eng-software
Repositório referente a matéria de engenharia de software

## Setup

Clone o repositório:

```bash
git clone git@github.com:guissalustiano/lab-eng-software.git
```

Mude para o diretório do projeto:

```bash
cd lab-eng-software
```

Crie o Venv:
```bash
python -m venv env
```

Ative o Venv:

No mac ou linux:
```bash
source env/bin/activate
```

No windows:
```bash
source env/Scripts/Activate.ps1
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Crie o projeto no django
```bash
django-admin startproject MyProj
```

## Execução

Após o setup, para executar o projeto, basta executar os seguintes comandos para executar a aplicação:

mudar para a pasta src
```bash
cd src
```

iniciar o servidor
```bash
python manage.py runserver
```

