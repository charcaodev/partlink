# app/analytics/api/assets.py

from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.repositories.assets_repository import AssetRepository
from app.services.assets_service import AssetService

from app.schemas.assets import (
    AssetResponse,
    AssetListResponse,
    AssetHealthSummaryResponse,
    AssetStatusCountResponse
)

router = APIRouter()


# =========================
# Dependency Injection
# =========================

def get_asset_service(
    db: Session = Depends(get_db)
) -> AssetService:

    repository = AssetRepository(db)
    return AssetService(repository)

@router.get(
    "/",

)
def list_assets(
):
    return {"message": "This endpoint will list all assets. Implementation pending."}

# =========================
# ANALYTICS ROUTES (STATIC FIRST)
# =========================

@router.get(
    "/health-summary",
    response_model=AssetHealthSummaryResponse
)
def get_asset_health_summary(
    asset_service: AssetService = Depends(get_asset_service)
):
    return asset_service.get_asset_health_summary()


@router.get(
    "/status-count",
    response_model=list[AssetStatusCountResponse]
)
def get_asset_count_by_status(
    asset_service: AssetService = Depends(get_asset_service)
):
    return asset_service.get_asset_count_by_status()


@router.get(
    "/critical-assets",
    response_model=AssetListResponse
)
def get_critical_assets(
    threshold: int = Query(default=40),
    asset_service: AssetService = Depends(get_asset_service)
):
    return asset_service.get_critical_assets(threshold)


# =========================
# QUERY ROUTES
# =========================

@router.get(
    "/search",
    response_model=AssetListResponse
)
def search_assets(
    model: str | None = Query(default=None),
    status: str | None = Query(default=None),
    asset_service: AssetService = Depends(get_asset_service)
):
    return asset_service.search_assets(
        model=model,
        status=status
    )


@router.get(
    "/site/{site_id}",
    response_model=AssetListResponse
)
def get_assets_by_site(
    site_id: UUID,
    asset_service: AssetService = Depends(get_asset_service)
):
    return asset_service.get_assets_by_site(site_id)


@router.get(
    "/status/{status}",
    response_model=AssetListResponse
)
def get_assets_by_status(
    status: str,
    asset_service: AssetService = Depends(get_asset_service)
):
    return asset_service.get_assets_by_status(status)


# =========================
# DYNAMIC ROUTES (MUST BE LAST)
# =========================

@router.get(
    "/{asset_id}",
    response_model=AssetResponse
)
def get_asset_by_id(
    asset_id: UUID,
    asset_service: AssetService = Depends(get_asset_service)
):

    asset = asset_service.get_asset_by_id(asset_id)

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )

    return asset