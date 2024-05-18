# 📌 Необходимо создать базу данных для интернет-магазина. База данных должна
# состоять из трех таблиц: товары, заказы и пользователи. Таблица товары должна
# содержать информацию о доступных товарах, их описаниях и ценах. Таблица
# пользователи должна содержать информацию о зарегистрированных
# пользователях магазина. Таблица заказы должна содержать информацию о
# заказах, сделанных пользователями.
# ○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
# имя, фамилия, адрес электронной почты и пароль.
# ○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
# название, описание и цена.
# ○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
# пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
# заказа.
# 📌 Создайте модели pydantic для получения новых данных и
# возврата существующих в БД для каждой из трёх таблиц
# (итого шесть моделей).
# 📌 Реализуйте CRUD операции для каждой из таблиц через
# создание маршрутов, REST API (итого 15 маршрутов).
# ○ Чтение всех
# ○ Чтение одного
# ○ Запись
# ○ Изменение
# ○ Удаление

import databases
import sqlalchemy
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from fastapi import FastAPI, Request
from model import User, UserIn, Product, ProductIn, Order, OrderIn
from typing import List

DATABASE_URL = 'sqlite:///database.db'

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32), index=True),
    sqlalchemy.Column("surname", sqlalchemy.String(32), index=True),
    sqlalchemy.Column("email", sqlalchemy.String(128), unique=True, index=True),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
    sqlalchemy.Constraint('order', relationship('orders', back_populates='user'))

)

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(50), index=True, unique=True),
    sqlalchemy.Column("description", sqlalchemy.String(255)),
    sqlalchemy.Column("price", sqlalchemy.Float),

)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("id_user", sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column('id_product', sqlalchemy.ForeignKey("products.id")),
    sqlalchemy.Column('date_order', sqlalchemy.DateTime(timezone=True), server_default=func.now()),
    sqlalchemy.Column('status_order', sqlalchemy.Boolean, default=False),
    sqlalchemy.Constraint('user', relationship('users', back_populates='order'))

)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")  # create db
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# region Users

@app.get('/users', response_model=List[User])
async def list_users(request: Request):
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def get_user(user_id: int, request: Request):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post('/users/', response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


# endregions

# region Products

@app.get("/products/", response_model=List[Product])
async def get_list_product():
    query = products.select()
    return await database.fetch_all(query)


@app.get('/products/{product_id}', response_model=Product)
async def get_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@app.post('/products/', response_model=ProductIn)
async def create_product(product: ProductIn):
    query = products.insert().values(**product.dict())
    last_record_id = await database.execute(query)
    return {**product.dict(), "id": last_record_id}


@app.put('/products/{product_id}', response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@app.delete('/products/{product_id}')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'massage': 'Product delete'}


# endregion

# region Orders


@app.get('/orders/', response_model=List[Order])
async def get_list_order():
    query = orders.select()
    return await database.fetch_all(query)


@app.get('/orders/{order_id}', response_model=Order)
async def get_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.put('/orders/{order_id}', response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id, "date_order": datetime.now()}


@app.post('/orders/{user_id}/{product_id}/', response_model=OrderIn)
async def create_order(user_id: int, product_id: int, order: OrderIn):
    query = orders.insert().values(id_user=user_id,
                                   id_product=product_id,
                                   status_order=order.status_order)
    last_record_order = await database.execute(query)
    return {**order.dict(), "id": last_record_order}


@app.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {"message": "Order deleted"}

# endregion
