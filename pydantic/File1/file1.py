from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    print: float
    is_avail: bool

input_data = {
    "id": 1,
    "name": "Laptop",
    "print": 50000,
    "is_avail": True
}

pro1 = Product(**input_data)
print(pro1)
