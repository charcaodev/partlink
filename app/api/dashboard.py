from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.dashboard_service import DashboardService
from app.schemas.dashboard import DashboardOverviewResponse

router = APIRouter()
service = DashboardService()

@router.get(
    "/overview",
    response_model=DashboardOverviewResponse
)
async def get_dashboard_overview(
    db: Session = Depends(get_db)
):
    return service.get_overview(db)
