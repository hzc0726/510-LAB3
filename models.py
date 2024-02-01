# models.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Task(BaseModel):
    name: str
    description: Optional[str] = None
    is_done: Optional[bool] = False
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    category: Optional[str] = None
