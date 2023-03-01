from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get('/users')
def get_users():
    return [{"id":1, "name" :"Eduardo"}]
    #return conn.execute(users.select()).fetchall()

#@user.post('/users')
#def create_user(user: User):
    
    #return conn.execute(users.select()).fetchall()


@user.get('/user')
def get_user():
    return {'hola'} 

@user.post('/user')
def create_user(user: User):
    new_user =  {"name" : user.name, "email": user.email }
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    print(new_user)
    result = conn.execute(users.insert().values(new_user))
    #print(result)

       