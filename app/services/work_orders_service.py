from app.schemas.work_orders import WorkOrderSummaryResponse, MonthlyWorkOrdersResponse, MonthlyWorkOrderData

from app.repositories.work_orders_repository import WorkOrdersRepository

class WorkOrderService:
    def __init__(self):
        self.repository = WorkOrdersRepository()

    def get_summary(self) -> WorkOrderSummaryResponse:
        summary = self.repository.get_work_orders_summary()
        return WorkOrderSummaryResponse(
            total_work_orders=summary["total_work_orders"],
            open_work_orders=summary["open_work_orders"],
            closed_work_orders=summary["closed_work_orders"]
        )

    def get_monthly_work_orders(self) -> MonthlyWorkOrdersResponse:
        monthly_data = [
            MonthlyWorkOrderData(month="2026-01", count=523),
            MonthlyWorkOrderData(month="2026-02", count=487),
            MonthlyWorkOrderData(month="2026-03", count=601)
        ]
        return MonthlyWorkOrdersResponse(monthly_work_orders=monthly_data)