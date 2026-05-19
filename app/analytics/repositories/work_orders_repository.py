from sqlalchemy.orm import Session
from sqlalchemy import func

from app.analytics.models.work_orders import (
    WorkOrder
)


class WorkOrdersRepository:

    # def get_total_work_orders(
    #     self,
    #     db: Session
    # ) -> int:

    #     total = db.query(
    #         func.count(WorkOrder.id)
    #     ).scalar()

    #     return total or 0
