from sqlalchemy.orm import Session

from app.repositories.asset_repository import AssetRepository
from app.schemas.assets import AssetSummaryResponse


class AssetService:
    def __init__(self):
        self.repository = AssetRepository()

    def get_summary(self, db: Session) -> AssetSummaryResponse:
        summary = self.repository.get_asset_summary(db)
        return AssetSummaryResponse(
            total_assets=summary["total_assets"],
            avg_uptime=summary["avg_uptime"],
            total_failures=summary["total_failures"],
        )
