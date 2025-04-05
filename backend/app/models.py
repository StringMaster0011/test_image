from pydantic import BaseModel
from typing import Optional

# Schema for reading item data (e.g., from the DB)
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True  # allows using ORM objects directly (if needed)

# Schema for creating a new item
class CreateItem(BaseModel):
    name: str
    description: Optional[str] = None
