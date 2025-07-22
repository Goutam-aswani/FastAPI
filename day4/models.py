from sqlalchemy import Column, Integer, String, Float
from db import Base

class Intern(Base):
    __tablename__ = "interns"

    id = Column(Integer,primary_key=True,index= True)
    name = Column(String)
    gender = Column(String)
    stipend = Column(Float)


