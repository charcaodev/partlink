from pydantic import BaseModel
from typing import List

class WorkOrderSummaryResponse(BaseModel):
    open_work_orders: int
    closed_work_orders: int
    avg_repair_time_hours: float

class MonthlyWorkOrderData(BaseModel):
    month: str  # format: "YYYY-MM"
    count: int

class MonthlyWorkOrdersResponse(BaseModel):
    monthly_work_orders: List[MonthlyWorkOrderData]
