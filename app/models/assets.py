from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from app.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Asset(Base):
    __tablename__ = "assets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    site_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    serial_number = Column(String, nullable=False, unique=True)
    model = Column(String, nullable=False)
    status = Column(String, nullable=False)
    health_score = Column(Integer, nullable=False, default=100)
    runtime_hours = Column(DateTime(timezone=True), nullable=False, default=0)
