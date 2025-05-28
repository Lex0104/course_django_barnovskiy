# course_django_barnovskiy

Заголовок: Проект Habits reminder - сервер вырабатывания хороших привычек
Описание: Цель и основные функции проекта.
Установка: Технологии:
python 3.13
django (>=5.2.1,<6.0.0)
djangorestframework (>=3.16.0,<4.0.0)
celery (>=5.5.2,<6.0.0)
PostgreSQL
Redis
Docker, Docker Compose

Инструкция для развертывания проекта:

Клонирование проекта:

git@github.com:Lex0104/course_django_barnovskiy.git
Создать виртуальное окружение:

python3 -m venv venv
Активировать виртуальное окружение:

source venv/bin/activate
Установить зависимости:
pip install -r pyproject.toml

Откройте проект в PyCharm, настройте базу данных в settings.py и выполните миграции:
python3 manage.py migrate

Запуск программы
python3 manage.py runserver

Для корректной работы проекта, требуется файл .env, который содержит переменные окружения:

Для настройки файла, в корне проекта создайте файл .env и заполните его переменными окружения указанными в файле env.sample

Запуск программы

python3 manage.py runserver