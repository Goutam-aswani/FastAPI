from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Intern(BaseModel):
    name : str
    gender : str
    stipend : float

interns : List[Intern] = []

@app.get("/")
async def welcome():
    return {"message":"welcome to home page"}

@app.get("/interns/")
async def get_interns():
    return {"interns" : interns}

@app.post("/interns/")
async def add_intern(intern: Intern):
    interns.append(intern)
    return {"message": "Intern added successfully"}

@app.put("/interns/{intern_id}")
async def update_intern(intern_id : int, intern : Intern):
    if 0 <= intern_id <=len(interns):
        interns[intern_id] =  intern
        return {"message" : "intern updated successfully"}
    return {"error": "Intern not found"}, 404

@app.delete("/interns/{intern_id}")
async def delete_intern(intern_id:int):
    if 0 <= intern_id <=len(interns):
        deleted = interns.pop(intern_id)
        return {f"message": "deleted intern with id {intern_id}", "deleted_intern": deleted} 
    return {"error": "Intern not found"}, 404

@app.get("/interns/{intern_id}")
async def get_intern(intern_id:int):
    if 0 <= intern_id < len(interns):
        return {"intern": interns[intern_id]}
    return {"error": "Intern not found"}, 404