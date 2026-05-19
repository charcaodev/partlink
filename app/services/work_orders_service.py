from app.schemas.work_orders import WorkOrderSummaryResponse, MonthlyWorkOrdersResponse, MonthlyWorkOrderData

class WorkOrderService:
    def get_summary(self) -> WorkOrderSummaryResponse:
        # MOCK DATA
        # later this comes from repository/database
        return WorkOrderSummaryResponse(
            open_work_orders=214,
            closed_work_orders=1820,
            avg_repair_time_hours=6.4
        )
    def get_monthly_work_orders(self) -> MonthlyWorkOrdersResponse:
        monthly_data = [
            MonthlyWorkOrderData(month="2026-01", count=523),
            MonthlyWorkOrderData(month="2026-02", count=487),
            MonthlyWorkOrderData(month="2026-03", count=601)
        ]
        return MonthlyWorkOrdersResponse(monthly_work_orders=monthly_data)
