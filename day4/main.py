from fastapi import FastAPI,Depends,Body,HTTPException
from sqlalchemy.orm import Session
import models,schemas,CRUD
from db import SessionLocal,engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Intern Management API"}

@app.get("/interns", response_model=list[schemas.InterOut])
def read_interns(db: Session = Depends(get_db)):
    interns = CRUD.get_interns(db)
    return interns

@app.get("/interns/{intern_id}", response_model=schemas.InterOut)
def read_intern(intern_id: int,db: Session = Depends(get_db)):
    intern = CRUD.get_intern(db, intern_id)
    if not intern:
        raise HTTPException(status_code=404, detail="Intern not found")
    return intern

@app.post("/interns", response_model=schemas.InterOut)
def create_intern(intern: schemas.InternCreate,
 db: Session = Depends(get_db),):
    return CRUD.create_intern(db, intern)

@app.put("/interns/{intern_id}", response_model=schemas.InterOut)
def update_intern(intern_id: int, updated: schemas.InternCreate, db:Session = Depends(get_db)):
        intern = CRUD.update_intern(db, intern_id, updated)
        if not intern:
            raise HTTPException(status_code=404, detail="Intern not found")
        return intern

@app.delete("/interns/{intern_id}", response_model=schemas.InterOut)
def delete_intern(intern_id: int, db: Session = Depends(get_db)):
    intern = CRUD.delete_intern(db, intern_id)
    if not intern:
        raise HTTPException(status_code=404, detail="Intern not found")
    return intern


@app.get("/health")
def health_check(): 
    return {"status": "ok", "message": "API is running smoothly"}