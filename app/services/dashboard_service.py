from sqlalchemy.orm import Session

from app.services.assets_service import AssetService
from app.services.inventory_service import InventoryService
from app.services.parts_service import PartsService
from app.services.work_orders_service import WorkOrderService
from app.schemas.dashboard import DashboardOverviewResponse


class DashboardService:
    def __init__(self):
        self.asset_service = AssetService()
        self.inventory_service = InventoryService()
        self.parts_service = PartsService()
        self.work_order_service = WorkOrderService()

    def get_overview(self, db: Session) -> DashboardOverviewResponse:
        asset_summary = self.asset_service.get_summary(db)
        inventory_summary = self.inventory_service.get_summary(db)
        part_summary = self.parts_service.get_summary(db)
        work_order_summary = self.work_order_service.get_summary(db)
        return DashboardOverviewResponse(
            inventory_value=inventory_summary.total_inventory_value,
            open_work_orders=work_order_summary.open_work_orders,
            critical_shortages=inventory_summary.critical_shortages,
            monthly_consumption=part_summary.monthly_consumption,
            asset_uptime=asset_summary.avg_uptime,
        )
