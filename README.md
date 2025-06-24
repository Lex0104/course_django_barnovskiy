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



ИСПОЛЬЗОВАНИЕ НА УДАЛЕННОМ СЕРВЕРЕ С docker-compose

НАСТРОЙКА СЕРВЕРА

1. Откройте терминал и выполните команду для обновления списка пакетов на сервере: sudo apt update
2. Затем выполните команду для обновления всех установленных пакетов до их последних версий: sudo apt upgrade
3. Установите Docker
4. Проверьте состояние файрвола с помощью команды: sudo ufw status и если фаервол отключен, активируйте его: sudo ufw enable
5. Откройте необходимые порты: sudo ufw allow 80/tcp sudo ufw allow 443/tcp sudo ufw allow 22/tcp


ИСПОЛЬЗОВАНИЕ ПРОЕКТА С АВТОМОТИЧЕСКИМ ДЕПЛОЕМ

НАСТРОЙКА СЕРВЕРА

1. Откройте терминал и выполните команду для обновления списка пакетов на сервере: sudo apt update
2. Затем выполните команду для обновления всех установленных пакетов до их последних версий: sudo apt upgrade
3. Установите Docker
4. Проверьте состояние файрвола с помощью команды: sudo ufw status и если фаервол отключен, активируйте его: sudo ufw enable
5. Откройте необходимые порты: sudo ufw allow 80/tcp sudo ufw allow 443/tcp sudo ufw allow 22/tcp

В проекте настроен файл GitHub Actions workflow(.github/workflows/ci.yaml). Благодаря этому при каждом push проекта запускается линтер flake8, запускаются тесты и проект деплоится на удалённый сервер после успешного прохождения тестов. Для корректной работы необходимо настроить секреты в вашем репозитории в GitHub.

Создайте секреты: SECRET_KEY, SERVER_IP, SSH_KEY, SSH_USER, TG_TOKEN
В сервисах 'web', 'celery', 'celery-beat' в строке image укажите свой DOCKER_HUB_USERNAME
