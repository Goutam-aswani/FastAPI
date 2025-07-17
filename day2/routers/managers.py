from fastapi import FastAPI,APIRouter
from pydantic import List
from fastapi.responses import JSONResponse
from ..models import models

Manager = models.Managar
router = APIRouter(prefix= "/manager",tags = ["manager"])

@router.get("/")
def view_managers():
    return JSONResponse(content={"message": "this is the list of managers"},status_code=222)

@router.post("/create")
def create_manager(manager:Manager):
    

