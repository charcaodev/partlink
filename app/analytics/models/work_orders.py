from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from app.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class WorkOrder(Base):
    __tablename__ = "work_orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    work_order_number = Column(String, nullable=False)
    status = Column(String)
    issue_type = Column(String)
    created_at = Column(DateTime(timezone=True), nullable=False)
    started_at = Column(DateTime(timezone=True), nullabe=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
