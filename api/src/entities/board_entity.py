from uuid import UUID

from pydantic import BaseModel


class BoardEntity(BaseModel):
    id: UUID
    name: str
