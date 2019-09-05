# Desafio técnico coopersystem

Controle de produtos e pedidos


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/kevinsantana/desafio-tecnico-coopersystem.git
cd desafio-tecnico-coopersystem
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
