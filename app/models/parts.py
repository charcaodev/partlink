from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Decimal
from app.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Parts(Base):
    __tablename__ = "parts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    part_number = Column(Integer, nullable=False, unique=True)
    description = Column(String, nullable=True)
    unit_cost = Column(Decimal, nullable=False, default=0)
    criticality = Column(String, nullable=True)
    lead_time_days = Column(Integer, nullable=True)
