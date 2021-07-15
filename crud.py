from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(id=user.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user.id).first()

    for var, value in vars(user).items():
        setattr(db_user, var, value) if value is not None else None

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
