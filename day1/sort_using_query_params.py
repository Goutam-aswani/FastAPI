from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union
import json
import os

app = FastAPI()

DATA_FILE = "data.json"


class Intern(BaseModel):
    id: int
    name: str
    age: int
    stipend: int
    gender: str
    internship_period: int

interns = [
  {
    "id": 1,
    "name": "Ananya Sharma",
    "age": 21,
    "stipend": 12000,
    "gender": "Female",
    "internship_period": 3
  },
  {
    "id": 2,
    "name": "Rohan Verma",
    "age": 22,
    "stipend": 15000,
    "gender": "Male",
    "internship_period": 3
  },
  {
    "id": 3,
    "name": "Meera Iyer",
    "age": 20,
    "stipend": 10000,
    "gender": "Female",
    "internship_period": 3
  },
  {
    "id": 4,
    "name": "Amit Joshi",
    "age": 23,
    "stipend": 14000,
    "gender": "Male",
    "internship_period": 3
  },
  {
    "id": 5,
    "name": "Sneha Kulkarni",
    "age": 21,
    "stipend": 11000,
    "gender": "Female",
    "internship_period": 3
  },
  {
    "id": 6,
    "name": "Kabir Singh",
    "age": 22,
    "stipend": 13000,
    "gender": "Male",
    "internship_period": 3
  },
  {
    "id": 7,
    "name": "Divya Nair",
    "age": 20,
    "stipend": 12500,
    "gender": "Female",
    "internship_period": 4
  },
  {
    "id": 8,
    "name": "Rahul Gupta",
    "age": 24,
    "stipend": 16000,
    "gender": "Male",
    "internship_period": 3
  },
  {
    "id": 9,
    "name": "Pooja Desai",
    "age": 21,
    "stipend": 13500,
    "gender": "Female",
    "internship_period": 4
  },
  {
    "id": 10,
    "name": "Nikhil Mehta",
    "age": 22,
    "stipend": 15000,
    "gender": "Male",
    "internship_period": 4
  }
]

@app.get("/")
async def get_interns():
    return interns

#query parameter
@app.get("/interns")
async def sort_interns(sort_by: Union[str, None] = None, order: Union[str, None] = None):
    if not sort_by and not order:
        return interns
    if not sort_by:
        return {"error": "Sort field is required"}, 400
    if not order:
        sorted_data = sorted(interns, key=lambda x: x[sort_by])
        return sorted_data
    if sort_by not in ["name", "age", "stipend"]:
        return {"error": "Invalid sort field"}, 400 
    if order not in ["asc", "desc"]:
        return {"error": "Invalid order"}, 400
    data = interns
    sort_order = False if order == "asc" else True
    sorted_data = sorted(data, key=lambda x: x[sort_by], reverse=sort_order)
    return sorted_data
