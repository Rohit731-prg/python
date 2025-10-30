# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

from pydantic import BaseModel
from typing import List

class Lessos(BaseModel):
    name: str

class Models(BaseModel):
    name: str
    Lesson: List[Lessos]

class Course(BaseModel):
    name: str
    Module: Models