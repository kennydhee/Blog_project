from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)




@router.get("/", response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


#Create Blog
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


#Delete Blog
@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(blog_id:int,db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.remove(blog_id, db)



#Update Blog
@router.put("/{blog_id}", status_code=status.HTTP_202_ACCEPTED)
def update(blog_id:int, request: schemas.Blog, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(blog_id, request, db)



# Extract using blog id
@router.get("/{blog_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(blog_id:int, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(blog_id,db)
