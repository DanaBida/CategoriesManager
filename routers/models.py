from pydantic import BaseModel

class Category(BaseModel):
    name: str
    region: str
    type: str