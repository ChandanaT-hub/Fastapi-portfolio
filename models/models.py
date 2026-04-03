from pydantic import BaseModel
from typing import List

class Experience(BaseModel):
    company: str
    role: str
    description: List[str]

class Portfolio(BaseModel):
    name: str
    role: str
    about: str
    skills: List[str]
    experience: List[Experience]