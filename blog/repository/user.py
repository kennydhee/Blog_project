from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from .. pwdhash import Hash


def create_account(request: schemas.User, db:Session):
    new_user = models.User(first_name=request.first_name, email=request.email, password=Hash.bcrypt
                           (request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(user_id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {user_id} does not exist")
    return user
