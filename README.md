# QRkot_spreadseets
Как развернуть проект на компьютере:
Клонировать репозиторий c GitHub на компьютер и перейти в него в командной строке
```$ git clone https://github.com/sunar87/QRkot.git```
```cd QRkot```
Создать и активировать виртуальное окружение:
# Windows
```$ python -m venv venv```
```$ source venv/Scripts/activate```

# Linux
python3 -m venv venv
source venv/bin/activate
Обновить менеджер пакетов pip
$ python -m pip install --upgrade pip
Установить зависимости из requirements.txt
$ pip install -r requirements.txt
Создать файл .env с переменными окружения. Пример наполнения:
DATABASE_URL=sqlite+aiosqlite:///./db.sqlite
SECRET=secret
Создать базу данных
$ alembic upgrade head
Запустить приложение
$ uvicorn app.main:app