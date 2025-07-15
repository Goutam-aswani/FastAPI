from fastapi import FastAPI
from pydantic import BaseModel,Field, EmailStr
from typing import List, Union

app = FastAPI()

class Intern(BaseModel):
    id: int = Field(..., description="Unique identifier for the intern")
    name: str = Field(..., min_length=1, max_length=100, description="Name of the intern")
    age: int = Field(..., ge=18, le=65, description="Age of the intern (between 18 and 65)")
    stipend: float = Field(..., gt=0, description="Monthly stipend amount (must be positive)")
    email: EmailStr = Field(..., description="Email address of the intern")

interns: List[Intern] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Intern Management System"}   

@app.post("/interns/")
def create_intern(intern: Intern):
    interns.append(intern)
    return {"message": "Intern created successfully", "intern": intern}

@app.get("/interns/")
def get_interns():  
    return {"interns": interns}

@app.get("/interns/{intern_id}")
def get_intern(intern_id: int):
    if 0 <= intern_id < len(interns):
        return {"intern": interns[intern_id]}
    return {"error": "Intern not found"}, 404

@app.put("/interns/{intern_id}")
def update_intern(intern_id: int, intern: Intern):
    if 0 <= intern_id < len(interns):
        interns[intern_id] = intern
        return {"message": "Intern updated successfully", "intern": intern}
    return {"error": "Intern not found"}, 404


@app.delete("/interns/{intern_id}")
def delete_intern(intern_id: int): 
    if 0 <= intern_id < len(interns):
        deleted = interns.pop(intern_id)
        return {"message": f"Deleted intern with id {intern_id}", "deleted_intern": deleted}
    return {"error": "Intern not found"}, 404


