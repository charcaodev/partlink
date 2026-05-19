from pydantic import BaseModel

class AssetSummaryResponse(BaseModel):
    total_assets: int
    avg_uptime: float
    total_failures: int

class AssetReliability(BaseModel):
    asset_id: str
    asset_name: str
    uptime_percentage: float
    failure_count: int
    downtime_hours: float

class AssetReliabilityResponse(BaseModel):
    assets: list[AssetReliability]
