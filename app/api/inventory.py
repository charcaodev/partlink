from app.services.inventory_service import InventoryService
from fastapi import APIRouter
from app.schemas.inventory import (
    InventorySummaryResponse,
    InventoryValueResponse
)

router = APIRouter()
service = InventoryService()

@router.get(
    "/summary",
    response_model=InventorySummaryResponse
)
async def get_inventory_summary():
    return service.get_summary()

@router.get(
    "/value",
    response_model=InventoryValueResponse)
async def get_inventory_value():
    return service.get_inventory_value()
