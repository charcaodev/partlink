from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.analytics.services.parts import PartService
from app.analytics.schemas.parts import TopPartsResponse

router = APIRouter()

part_service = PartService()

def get_parts_dashboard(db: Session = Depends(get_db)):
    return part_service.get_top_consumed_parts()
