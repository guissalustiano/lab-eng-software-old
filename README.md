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

**Os passos a seguir so são necessários se o projeto não estiver sido criado no repositório ainda**

Crie o projeto no django
```
django-admin startproject aviation_website_project
```

Crie o projeto no django
```
python manage.py startapp flight_monitoring_app
```

## Execução

### Inicialização do servidor


Após o setup, para executar o projeto, basta executar os seguintes comandos para executar a aplicação:

mudar para a pasta src
```
cd aviation_website_project
```

iniciar o servidor
```
python manage.py runserver
```

Visite a url http://127.0.0.1:8000/ para testar a aplicação.

Alguns logins que você pode utilizar são:
  - manager@mail.com
  - pilot@mail.com
  - operator@mail.com
  - admin@mail.com

Qualquer senha irá funcionar

### Migração

Para executar as migrações, crie as migrações com:
```
python manage.py makemigrations
```

Se você quiser ver o que o Django está criando, você pode usar o comando:
```
python manage.py sqlmigrate flight_monitoring_app numero # numero pode ser 0001, 0002, etc
```

E em seguida, execute as migrações com:
```
python manage.py migrate
```

## Testes

Para rodar os testes, execute o comando:
```
python manage.py test
```