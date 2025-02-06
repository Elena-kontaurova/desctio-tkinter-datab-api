''' апишка'''
# import fastapi as tk
from fastapi import FastAPI, HTTPException, Body
from connect import User, Document, Comment

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


def get_doc():
    ''' kjkj'''
    doc = Document.get()
    return doc

@app.get('/api/v1/Documents')
async def get_document():
    ''' вывод всех документов'''
    return get_doc()

def num_com_doc(id_n: int):
    ''' Получить информацию о документе '''
    doc = Document.get(Document.id == id_n)
    comments = list(Comment.select().where(Comment.document == doc))
    comments_list = [
        {
            'id': comment.id,
            'document_id': comment.document.id,
            'text': comment.text,
            'date_created': comment.date_created,
            'date_updated': comment.date_updated,
            'author': {
                'name': comment.author_name,
                'position': comment.author_position
            }
        } for comment in comments
    ]
    return {
        'id': doc.id,
        'title': doc.title,
        'date_created': doc.date_created,
        'date_updated': doc.date_updated,
        'category': doc.category,
        'has_comments': doc.has_comments,
        'comments': comments_list  # Добавляем список комментариев
    }

# pylint: disable=C0103
@app.get('/api/v1/Document/{documentId}/Comments')
async def get_number_com(documentId: int):
    ''' Получить список комментариев к документу'''
    return num_com_doc(id_n=documentId)
