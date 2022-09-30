# lab-eng-software
Repositório referente a matéria de engenharia de software

nome do grupo: 
- Grupo 8

nome dos integrantes:
- Ricardo de Arruda
- Guilherme Stabach Salustiano
- Sander Söhngen Rodrigues

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
./env/Scripts/Activate.ps1
```

Instale as dependências:
```
pip install -r requirements.txt
```

**O passo a seguir so é necessário se o projeto não estiver sido criado no repositório ainda**

Crie o projeto no django
```
django-admin startproject src
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

Visit a url http://127.0.0.1:8000/FIRST para acessar a aplicação.
