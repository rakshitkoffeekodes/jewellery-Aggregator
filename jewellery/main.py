from sqlalchemy.orm import Session
from seller import models
from seller.database import engine, SessionLocal
from fastapi import FastAPI, Depends, Form
from fastapi.responses import JSONResponse

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#
# @app.post('/add_permission/')
# def add_permission(name: str = Form(), codename: str = Form(), db: Session = Depends(get_db)):
#     new_permission = models.Permission(
#         name=name,
#         codename=codename
#     )
#     db.add(new_permission)
#     db.commit()
#     return JSONResponse({'message': 'add permission successfully.'})
#
#
@app.post('/user_request/')
def user_request(user_name: str = Form(),
                 user_surname: str = Form(),
                 user_email: str = Form(),
                 user_mobile_number: str = Form(),
                 user_gst_number: str = Form(),
                 user_shop_name: str = Form(),
                 user_address: str = Form(),
                 user_city: str = Form(),
                 user_state: str = Form(),
                 # status: str = Form(),
                 # description: str = Form(),
                 role: str = Form(),
                 password: str = Form(),
                 confirm_password: str = Form(),
                 db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.user_email == user_email).first()
        if not user:
            if password == confirm_password:
                new_user = models.User(
                    user_name=user_name,
                    user_surname=user_surname,
                    user_email=user_email,
                    user_mobile_number=user_mobile_number,
                    user_gst_number=user_gst_number,
                    user_shop_name=user_shop_name,
                    user_address=user_address,
                    user_city=user_city,
                    user_state=user_state,
                    role=role,
                    user_password=password
                )
                db.add(new_user)
                db.commit()
                new_request = models.UserRequest(
                    user_id=new_user.user_id
                )
                db.add(new_request)
                db.commit()
                return JSONResponse({'message': 'User Request Sending Successfully.'})
            else:
                return JSONResponse({'message': 'Password not match'})
        else:
            return JSONResponse({'message': 'email is already exist'})
    except Exception as e:
        return JSONResponse({'message': e.__str__()})


