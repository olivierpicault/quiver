import uuid

from sqlalchemy.dialects.postgresql import UUID

from database import db
from src.models.timestamp_mixin import TimestampMixin


class Board(db.Model, TimestampMixin):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
