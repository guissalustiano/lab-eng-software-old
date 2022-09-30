# lab-eng-software
Repositório referente a matéria de engenharia de software

## Setup

Clone o repositório:

```
git clone git@github.com:guissalustiano/lab-eng-software.git
```

Mude para o diretório do projeto:

```
cd lab-eng-software
```

Crie o Venv:
```
python -m venv env
```

Ative o Venv:

No mac ou linux:
```
source env/bin/activate
```

No windows:
```
source env/Scripts/Activate.ps1
```

Instale as dependências:
```
pip install -r requirements.txt
```

Crie o projeto no django
```
django-admin startproject MyProj
```

## Execução

Após o setup, para executar o projeto, basta executar os seguintes comandos para executar a aplicação:

mudar para a pasta src
```
cd src
```

iniciar o servidor
```
python manage.py runserver
```

