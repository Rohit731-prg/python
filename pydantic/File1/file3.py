from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Union, Annotated

class Cart(BaseModel):
    user_id: int
    address: Annotated[str, Field(min_length=5, max_length=50)]
    products: List[Dict[str, Optional[Union[str, int]]]]
    image: Optional[str] = None

rohit = Cart(
    user_id=1,
    address="Del",
    products=[
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Mobile"}
    ]
)
print(rohit)
