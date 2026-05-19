from app.analytics.services.work_orders_service import WorkOrderService
from fastapi import APIRouter

from app.analytics.schemas.work_orders import (
    WorkOrderSummaryResponse,
    MonthlyWorkOrdersResponse,
    MonthlyWorkOrderData
)

router = APIRouter()

service = WorkOrderService()


@router.get(
    "/overview",
    response_model=WorkOrderSummaryResponse
)
async def get_dashboard_overview(

):

    return service.get_summary()