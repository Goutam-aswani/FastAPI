from fastapi import FastAPI
from pydantic import BaseModel  
from typing import List

from requests import get

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    department: str


@app.get("/")
def read_root():
    return {"message": "This is a simple FastAPI application."}

students: List[Student] = []

@app.post("/students/")
def create_student(student: Student):
    students.append(student)
    return {"message": "Student created successfully", "student": student}

@app.get("/students/")
def get_students():     
    return {"students": students}     

@app.get("/students/{student_id}")
def get_student(student_id: int):   
    if 0 <= student_id < len(students):
        return {"student": students[student_id]}
    return {"error": "Student not found"}, 404

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):      
    if 0 <= student_id < len(students):
        students[student_id] = student
        return {"message": "Student updated successfully", "student": student}
    return {"error": "Student not found"}, 404

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    deleted = students.pop(student_id)
    if deleted is not None:
        return {"message": "Student deleted successfully"}
    return {"error": "Student not found"}, 404