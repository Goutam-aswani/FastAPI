from fastapi import FastAPI , APIRouter
from pydantic import BaseModel, Field, EmailStr

router = APIRouter(prefix = "/intern", tags = ["intern"])

@router.get("/")
def get_interns():
    return {"message": "List of interns"}
