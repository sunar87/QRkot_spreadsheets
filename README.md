# QRkot_spreadsheets
QRKot - это приложение для Благотворительного фонда, реализованное на фреймворке FastAPI.
Цель проекта - отработать навыки работы с FastAPI, SQLAlchemy и GoogleAPI.

Используемые технологии: 
python, FastApi, SQLAlchemy, Alembic
## Как развернуть проект на компьютере

### 1. Клонировать репозиторий с GitHub на компьютер и перейти в него в командной строке

```sh
git clone https://github.com/sunar87/QRkot.git
cd QRkot
2. Создать и активировать виртуальное окружение
python -m venv venv
source venv/Scripts/activate
3. Обновить менеджер пакетов pip
python -m pip install --upgrade pip
4. Установить зависимости из requirements.txt
pip install -r requirements.txt
5. Создать файл .env с переменными окружения
DATABASE_URL=sqlite+aiosqlite:///./db.sqlite
SECRET=secret
6. Создать базу данных
alembic upgrade head
7. Запустить приложение
uvicorn app.main:app

Автор проекта
Студент Яндекс.Практикум,
Войтов Семён 
https://github.com/sunar87/