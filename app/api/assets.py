from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.asset_service import AssetService
from app.schemas.assets import AssetSummaryResponse

router = APIRouter()
service = AssetService()

@router.get(
    "/summary",
    response_model=AssetSummaryResponse
)
async def get_asset_summary(
    db: Session = Depends(get_db)
):
    return service.get_summary(db)
