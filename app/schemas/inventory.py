from pydantic import BaseModel
from typing import List

class InventorySummaryResponse(BaseModel):
    total_parts: int
    parts_in_stock: int
    parts_out_of_stock: int
    avg_restock_time_days: float

class InventoryValueResponse(BaseModel):
    total_inventory_value: float
    average_part_cost: float
