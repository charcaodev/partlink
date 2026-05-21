# app/schemas/assets.py

from uuid import UUID
from typing import Optional, List

from pydantic import BaseModel, Field


# =========================
# Asset Response
# =========================

class AssetResponse(BaseModel):
    id: UUID
    site_id: UUID
    serial_number: str
    model: str
    status: str
    health_score: int = Field(ge=0, le=100)
    runtime_hours: float

    class Config:
        from_attributes = True


# =========================
# Asset List Response
# =========================

class AssetListResponse(BaseModel):
    assets: List[AssetResponse]


# =========================
# Asset Status Count
# =========================

class AssetStatusCountResponse(BaseModel):
    status: str
    count: int


# =========================
# Asset Health Summary
# =========================

class AssetHealthSummaryResponse(BaseModel):
    total_assets: int
    average_health_score: float
    critical_assets: int


# =========================
# Asset Search Filters
# =========================

class AssetSearchFilters(BaseModel):
    model: Optional[str] = None
    status: Optional[str] = None