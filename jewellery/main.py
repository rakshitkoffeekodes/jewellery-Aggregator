from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import Session
from seller import models
from seller.database import engine, SessionLocal
from fastapi import FastAPI, Depends, Form
from fastapi.responses import JSONResponse
from seller.models import *

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post('/create_user/')
def create_user(
        name: str = Form(),
        surname: str = Form(),
        email: str = Form(),
        role: str = Form(),
        group: str = Form(),
        password: str = Form(),
        confirm_password: str = Form(),
        db: Session = Depends(get_db)
):
    user_email = db.query(User).filter(User.email == email).first()
    if user_email:
        return JSONResponse({'message': 'Email is already exist'})
    else:
        if password == confirm_password:
            new_user = User(
                name=name,
                surname=surname,
                email=email,
                role=role,
                group=group,
                password=password,
                register_date=datetime.now()
            )
            db.add(new_user)
            db.commit()
            return JSONResponse({'message': 'User register successfully.', 'data': new_user.as_dict()})
        else:
            return JSONResponse({'message': 'your password is not match'})
