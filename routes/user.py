from fastapi import APIRouter
from models.user import users
from config.db import conn
from schemas.user import User

user = APIRouter()

@user.get('/')
async def fetch_users():
    return conn.execute(users.select()).fetchall()

@user.get('/{id}')
async def fetch_user(id: int):
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.post('/')
async def create_users(user : User): #gets the schema type on its own
    conn.execute(users.insert().values(
        name = user.name,
        email = user.email,
        password = user.password
    ))
    return conn.execute(users.select()).fetchall()


@user.put('/{id}')
async def fetch_users(id: int, user:User): #gets the user schema auto and ask for id
    conn.execute(users.update().values(
        name = user.name,
        email= user.email,
        password = user.password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

@user.delete('/{id}')
async def delete_user(id : int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()