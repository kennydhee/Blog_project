from fastapi import APIRouter, Depends, status
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)




#Create User
@router.post("/", response_model=schemas.ShowUser)
def create_account(request:schemas.User, db: Session = Depends(database.get_db)):
    return user.create_account(request, db)


#Get User with id
@router.get("/{user_id}", response_model=schemas.ShowUser)
def get_user(user_id:int, db: Session = Depends(database.get_db)):
    return user.get_user(user_id, db)