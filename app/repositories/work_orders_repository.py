from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.work_orders import WorkOrder

class WorkOrdersRepository:

    def get_work_orders_summary(self, db: Session):
        total_work_orders = db.query(WorkOrder).count()
        open_work_orders = db.query(WorkOrder).filter(WorkOrder.status == "open").count()
        closed_work_orders = db.query(WorkOrder).filter(WorkOrder.status == "closed").count()
        return {
            "total_work_orders": total_work_orders,
            "open_work_orders": open_work_orders,
            "closed_work_orders": closed_work_orders
        }
    
    def get_work_orders_by_priority(self, db: Session):
        
        open_work_orders = db.query(WorkOrder).filter(WorkOrder.status == "open").all()
        in_progress_orders = db.query(WorkOrder).filter(WorkOrder.status == "in_progress").all()
        

        return {
            "low": open_work_orders_by_priority["low"] + in_progress_orders_by_priority["low"],
            "medium": open_work_orders_by_priority["medium"] + in_progress_orders_by_priority["medium"],
            "high": open_work_orders_by_priority["high"] + in_progress_orders_by_priority["high"]
        }      



    