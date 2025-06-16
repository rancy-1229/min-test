from typing import Optional

from sqlmodel import SQLModel, Field


class Fruits(SQLModel, table=True):
    __tablename__ = "fruits"
    id: int = Field(primary_key=True)
    name: Optional[str]
    color: Optional[str]
