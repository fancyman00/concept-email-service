from __future__ import annotations
from pydantic import BaseModel


class Message(BaseModel):
    name: str
    phone: str
    email: str
    message: str
