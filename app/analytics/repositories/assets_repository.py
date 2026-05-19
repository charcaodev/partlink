from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.asset import Asset


class AssetRepository:

    def get_asset_summary(self, db: Session):

        total_assets = db.query(Asset).count()

        avg_uptime = (
            db.query(func.avg(Asset.uptime_percentage))
            .scalar()
        )

        total_failures = (
            db.query(func.sum(Asset.failure_count))
            .scalar()
        )

        return {
            "total_assets": total_assets,
            "avg_uptime": avg_uptime or 0,
            "total_failures": total_failures or 0
        }

    def get_asset_reliability(self, db: Session):

        assets = db.query(Asset).all()

        return assets