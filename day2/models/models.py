from fastapi import FastAPI
from pydantic import BaseModel,Field

class Intern(BaseModel):
    name : str = Field(min_length=3,max_length=100)
    age : int = Field(ge = 18 , le = 65)
    stipend : int = Field (description= "this shows the stipend of the intern")

class Managar(BaseModel):
    name : str = Field(min_length=3,max_length=100)
    age : int = Field(ge = 18 , le = 65)
    project : str = Field (description= "this shows the project")



