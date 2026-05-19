from app.schemas.inventory import InventorySummaryResponse, InventoryValueResponse

class InventoryService:
    def get_summary(self) -> InventorySummaryResponse:
        # MOCK DATA
        # later this comes from repository/database
        return InventorySummaryResponse(
            total_parts=12500,
            parts_in_stock=9800,
            parts_out_of_stock=2700,
            avg_restock_time_days=4.2
        )
    def get_inventory_value(self) -> InventoryValueResponse:
        # MOCK DATA
        # later this comes from repository/database
        return InventoryValueResponse(
            total_inventory_value=350000.00,
            average_part_cost=28.00
        )
