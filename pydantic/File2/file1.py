from pydantic import BaseModel, field_validator, model_validator, computed_field

class Test(BaseModel):
    username: str
    @field_validator("username")
    def username_length(cls, v):
        if len(v) < 3:
            raise ValueError("username must be at least 3 characters long")
        return v
    
class signUp(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("passwords do not match")
        return values
    
class Product(BaseModel):
    quantity: int
    price: int

    @computed_field
    @property
    def total_price(self):
        return self.quantity * self.price