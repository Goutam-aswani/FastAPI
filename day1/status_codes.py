from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/greet")
def create_greeting(name: str):
    return {"message": f"Hello {name}!"}

@app.post("/custom_response")
def custom_response(name: str):
    return JSONResponse(content={"message": f"Hello {name}!"}, status_code=201)

@app.get("/custom-error")
def custom_error():
    return JSONResponse(content={"error": "This is a custom error message"}, status_code=424)



