from sqlalchemy.orm import Session
from sqlalchemy import func

from app.analytics.models.inventory import (
    Inventory
)


class InventoryRepository:

    # def get_total_inventory_items(
    #     self,
    #     db: Session
    # ) -> int:

    #     total = db.query(
    #         func.count(Inventory.id)
    #     ).scalar()

    #     return total or 0
