from pydantic import BaseModel
from typing import List, Dict, Optional, Union

class Cart(BaseModel):
    user_id: int
    products: List[Dict[str, Optional[Union[str, int]]]]
    image: Optional[str] = None

rohit = Cart(user_id=1, products=[{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Mobile"}])
print(rohit)