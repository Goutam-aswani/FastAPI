from fastapi import FastAPI
from sqlalchemy.orm import Session
import models,schemas

def get_interns(db:Session):
    return db.query(models.Intern).all()

def get_intern(db: Session, intern_id: int):
    return db.query(models.Intern).filter(models.Intern.id == intern_id).first()

def create_intern(db: Session, intern: schemas.InternCreate):
    db_intern = models.Intern(**intern.dict())
    db.add(db_intern)
    db.commit()
    db.refresh(db_intern)
    return db_intern

def update_intern(db: Session, intern_id: int, updated: schemas.InternCreate):
    intern = db.query(models.Intern).filter(models.Intern.id == intern_id).first()
    if intern:
        intern.name = updated.name
        intern.gender = updated.gender
        intern.stipend = updated.stipend
        db.commit()
        db.refresh(intern)
    return intern

def delete_intern(db: Session, intern_id: int):
    intern = db.query(models.Intern).filter(models.Intern.id == intern_id).first()
    if intern:
        db.delete(intern)
        db.commit()
    return intern

