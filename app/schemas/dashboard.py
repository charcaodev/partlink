from pydantic import BaseModel

class DashboardOverviewResponse(BaseModel):
    inventory_value: float
    open_work_orders: int
    critical_shortages: int
    monthly_consumption: float
    asset_uptime: float