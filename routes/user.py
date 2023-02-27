from fastapi import APIRouter

user = APIRouter()

@user.get('/users')
def users_list():
    return {'hola'} 

@user.get('/users')
def users_list():
    return {'hola'} 

@user.get('/users')
def users_list():
    return {'hola'} 


@user.get('/users')
def users_list():
    return {'hola'}           