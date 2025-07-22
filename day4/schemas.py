from pydantic import BaseModel

class InternBase(BaseModel):
    name : str
    gender : str
    stipend : float

class InternCreate(InternBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "name": "goutam",
                "gender": "male",
                "stipend": 1500.0
            }
        }

class InterOut(InternBase):
    id : int
    class Config:
        orm_mode = True 