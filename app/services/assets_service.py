# app/services/asset_service.py

from uuid import UUID

from app.repositories.assets_repository import (
    AssetRepository
)

from app.schemas.assets import (
    AssetResponse,
    AssetListResponse,
    AssetHealthSummaryResponse,
    AssetStatusCountResponse
)

class AssetService:

    def __init__(
        self,
        assets_repository: AssetRepository
    ):
        self.assets_repository = assets_repository

    # =========================
    # ASSET LOOKUPS
    # =========================

    def get_asset_by_id(
        self,
        asset_id: UUID
    ) -> AssetResponse | None:

        asset = (
            self.assets_repository.get_asset_by_id(
                asset_id
            )
        )

        if not asset:
            return None

        return AssetResponse.model_validate(asset)

    def get_asset_by_serial_number(
        self,
        serial_number: str
    ) -> AssetResponse | None:

        asset = (
            self.assets_repository
            .get_asset_by_serial_number(
                serial_number
            )
        )

        if not asset:
            return None

        return AssetResponse.model_validate(asset)

    def get_assets_by_site(
        self,
        site_id: UUID
    ) -> AssetListResponse:

        assets = (
            self.assets_repository
            .get_assets_by_site(site_id)
        )

        return AssetListResponse(
            assets=[
                AssetResponse.model_validate(asset)
                for asset in assets
            ]
        )

    def get_assets_by_status(
        self,
        status: str
    ) -> AssetListResponse:

        assets = (
            self.assets_repository
            .get_assets_by_status(status)
        )

        return AssetListResponse(
            assets=[
                AssetResponse.model_validate(asset)
                for asset in assets
            ]
        )

    def search_assets(
        self,
        model: str | None = None,
        status: str | None = None
    ) -> AssetListResponse:

        assets = (
            self.assets_repository.search_assets(
                model=model,
                status=status
            )
        )

        return AssetListResponse(
            assets=[
                AssetResponse.model_validate(asset)
                for asset in assets
            ]
        )

    # =========================
    # ANALYTICS
    # =========================

    def get_asset_health_summary(
        self
    ) -> AssetHealthSummaryResponse:

        total_assets = (
            self.assets_repository
            .get_total_asset_count()
        )

        average_health_score = (
            self.assets_repository
            .get_average_health_score()
        )

        critical_assets = len(
            self.assets_repository
            .get_critical_assets()
        )

        return AssetHealthSummaryResponse(
            total_assets=total_assets,
            average_health_score=round(
                average_health_score or 0,
                2
            ),
            critical_assets=critical_assets
        )

    def get_asset_count_by_status(
        self
    ) -> list[AssetStatusCountResponse]:

        results = (
            self.assets_repository
            .get_asset_count_by_status()
        )

        return [
            AssetStatusCountResponse(
                status=status,
                count=count
            )
            for status, count in results
        ]

    def get_critical_assets(
        self,
        threshold: int = 40
    ) -> AssetListResponse:

        assets = (
            self.assets_repository
            .get_critical_assets(threshold)
        )

        return AssetListResponse(
            assets=[
                AssetResponse.model_validate(asset)
                for asset in assets
            ]
        )

    def get_high_runtime_assets(
        self,
        runtime_threshold: float
    ) -> AssetListResponse:

        assets = (
            self.assets_repository
            .get_high_runtime_assets(
                runtime_threshold
            )
        )

        return AssetListResponse(
            assets=[
                AssetResponse.model_validate(asset)
                for asset in assets
            ]
        )