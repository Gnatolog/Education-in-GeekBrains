# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс User с полями id, name, email и password.
# 📌 Создайте список users для хранения пользователей.
# 📌 Создайте маршрут для добавления нового пользователя (метод POST).
# 📌 Реализуйте валидацию данных запроса и ответа.
# 📌Создайте маршрут для обновления информации о пользователе (метод PUT).
# 📌Создайте маршрут для удаления информации о пользователе (метод DELETE).
# 📌 Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# 📌 Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# 📌 Создайте маршрут для отображения списка пользователей (метод GET).
# 📌 Реализуйте вывод списка пользователей через шаблонизатор Jinja.

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlalchemy
import databases
from model import User, UserIn

DATABASE_URL = 'sqlite:///my_database.db'
database = databases.Database(DATABASE_URL, )
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32), index=True),
    sqlalchemy.Column("email", sqlalchemy.String(128), unique=True, index=True),
    sqlalchemy.Column("password", sqlalchemy.String(128))
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()
templates = Jinja2Templates(directory="./templates")


@app.on_event("startup")  # create db
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name,
                                  email=user.email,
                                  password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(),
            "id": last_record_id}


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f'User delete'}


@app.get("/users", response_class=HTMLResponse)
async def get_list_user(request: Request):
    query = users.select()
    list_user = await database.fetch_all(query)
    return templates.TemplateResponse("home.html",
                                      {'request': request,
                                       'list_user': list_user})
