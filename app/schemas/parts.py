from pydantic import BaseModel
from typing import List

class PartsSummaryResponse(BaseModel):
    open_work_orders: int
    closed_work_orders: int
    avg_repair_time_hours: float
