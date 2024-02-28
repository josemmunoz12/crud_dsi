from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    name: str
    descripcion: str
    precio: int
