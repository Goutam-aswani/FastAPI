from fastapi import FastAPI, HTTPException
from routers import interns

app = FastAPI()

app.include_router(interns.router)

@app.get("/in")
def esehi():
    return {"hello"}

