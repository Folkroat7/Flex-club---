# Flex-club: Система записи в фитнес-клуб с API и веб-интерфейсом.

Пет-проект, реализующий стек Django+HTML/CSS/JS с встроенным API. Формализованная документация на Swagger доступна по адресу /api/docs
Стек технологий: Python 3.12, Django 6, DRF, Swagger, JavaScript.

Как запустить:
1. Клонировать репозиторий.
2. Создать venv и сделать pip install -r requirements.txt.
3. Сделать python manage.py migrate.
4. Запустить runserver.

---------------------------EN--------------------------------

Pet Project: Django + HTML/CSS/JS with Built-in API

A pet project implementing the Django + HTML/CSS/JS stack with a built‑in API.
Formal API documentation (Swagger) is available at /api/docs.

Tech stack:
Python 3.12, Django 6, DRF (Django Rest Framework), Swagger, JavaScript.

How to run
Clone the repository

bash
git clone <repository-url>
cd <project-folder>
Create a virtual environment and install dependencies

bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Apply migrations

bash
python manage.py migrate
Run the development server

bash
python manage.py runserver
The project will be available at http://127.0.0.1:8000/.
Swagger API docs can be accessed at http://127.0.0.1:8000/api/docs.
