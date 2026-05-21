# app/repositories/asset_repository.py

from uuid import UUID
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.assets import Asset


class AssetRepository:

    def __init__(self, db: Session):
        self.db = db

    # =========================
    # READ QUERIES
    # =========================

    def get_asset_by_id(
        self,
        asset_id: UUID
    ) -> Optional[Asset]:

        return (
            self.db.query(Asset)
            .filter(Asset.id == asset_id)
            .first()
        )

    def get_asset_by_serial_number(
        self,
        serial_number: str
    ) -> Optional[Asset]:

        return (
            self.db.query(Asset)
            .filter(Asset.serial_number == serial_number)
            .first()
        )

    def get_assets_by_site(
        self,
        site_id: UUID
    ) -> list[Asset]:

        return (
            self.db.query(Asset)
            .filter(Asset.site_id == site_id)
            .all()
        )

    def get_assets_by_status(
        self,
        status: str
    ) -> list[Asset]:

        return (
            self.db.query(Asset)
            .filter(Asset.status == status)
            .all()
        )

    def search_assets(
        self,
        model: Optional[str] = None,
        status: Optional[str] = None
    ) -> list[Asset]:

        query = self.db.query(Asset)

        if model:
            query = query.filter(Asset.model == model)

        if status:
            query = query.filter(Asset.status == status)

        return query.all()

    # =========================
    # ANALYTICS QUERIES
    # =========================

    def get_total_asset_count(self) -> int:

        return (
            self.db.query(func.count(Asset.id))
            .scalar()
        )

    def get_average_health_score(self) -> float:

        return (
            self.db.query(func.avg(Asset.health_score))
            .scalar()
        )

    def get_asset_count_by_status(self):

        return (
            self.db.query(
                Asset.status,
                func.count(Asset.id)
            )
            .group_by(Asset.status)
            .all()
        )

    def get_critical_assets(
        self,
        threshold: int = 40
    ) -> list[Asset]:

        return (
            self.db.query(Asset)
            .filter(Asset.health_score <= threshold)
            .all()
        )

    def get_high_runtime_assets(
        self,
        runtime_threshold: float
    ) -> list[Asset]:

        return (
            self.db.query(Asset)
            .filter(
                Asset.runtime_hours >= runtime_threshold
            )
            .all()
        )