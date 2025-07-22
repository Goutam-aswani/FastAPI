from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from sqlmodel import Session, create_engine, SQLModel, Field,select
from pydantic import BaseModel


class Intern(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = None
    stipend: float

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as db:
        yield db


@app.get("/interns/", response_model=list[Intern])
def read_interns(db: Session = Depends(get_db)):
    interns = db.exec(select(Intern)).all()
    return interns  



@app.post("/interns/", response_model=Intern)
async def create_intern(intern: Intern, db: Session = Depends(get_db)):
    db.add(intern)
    db.commit()
    db.refresh(intern)
    return intern

@app.get("/interns/{intern_id}", response_model=Intern)
def read_intern(intern_id: int, db: Session = Depends(get_db)):
    intern = db.get(Intern, intern_id)
    if not intern:
        raise HTTPException(status_code=404, detail="Intern not found")
    return intern

@app.put("/interns/{intern_id}", response_model=Intern)
def update_intern(intern_id: int, intern: Intern, db: Session = Depends(get_db)):
    db_intern = db.get(Intern, intern_id)
    if not db_intern:
        raise HTTPException(status_code=404, detail="Intern not found")
    for key, value in intern.dict(exclude_unset=True).items():
        setattr(db_intern, key, value)
    db.add(db_intern)
    db.commit()
    db.refresh(db_intern)
    return db_intern

@app.delete("/interns/{intern_id}", response_model=Intern)
def delete_intern(intern_id: int, db: Session = Depends(get_db)):
    intern = db.get(Intern, intern_id)
    if not intern:
        raise HTTPException(status_code=404, detail="Intern not found")
    db.delete(intern)
    db.commit()
    return intern
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)