from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    streat: str
    city: str
    state: str

class User(BaseModel):
    name: str
    age: int
    address: Address

class Comment(BaseModel):
    content: str
    user: User
    reply: Optional[List['Comment']] = None

Comment.model_rebuild()