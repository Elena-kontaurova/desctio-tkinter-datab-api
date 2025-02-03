''' апишка'''
# import fastapi as tk
from fastapi import FastAPI, HTTPException, Body
from connect import User

app = FastAPI()


def user_get(name: str):
    ''' получение логина и пароля'''
    user = User.get(User.name == name)
    return user


@app.post("/api/v1/SignIn")
async def sign_in(name: str = Body(...), password: str = Body(...)):
    ''' метод для авторизации '''
    user = user_get(name)
    if not user or user.password != password:
        raise HTTPException(status_code=403, detail="Некорректный логин, пароль")
    return {'msg': 'Вы успешно вошли в систему'}
