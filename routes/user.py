from fastapi import APIRouter
from models.user import users
from config.db import conn
user = APIRouter()

@user.get('/')
async def fetch_users():
    return conn.execute(users.select()).fetchall()