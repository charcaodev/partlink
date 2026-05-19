from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from app.core.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    parts_id = Column(UUID(as_uuid=True), ForeignKey("parts.id"), nullable=False)
    warehouse_name = Column(String, nullable=False)
    quantity_on_hand = Column(Integer, nullable=False, default=0)
    quantity_reserved = Column(Integer, nullable=False, default=0)
    reorder_point = Column(Integer, nullable=False)
