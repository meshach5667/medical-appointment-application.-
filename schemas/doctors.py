from pydantic import BaseModel
from typing import Optional

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True
