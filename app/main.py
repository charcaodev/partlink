from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import dashboard
from app.api import work_orders
from app.api import inventory
from app.api import assets

app = FastAPI(
    title="PartLink API",
    version="0.1.0",
    description="Analytics backend for OEM aftermarket platform"
)

# -------------------------
# CORS (React frontend)
# -------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# API ROUTES
# -------------------------

# app.include_router(
#     dashboard.router,
#     prefix="/analytics/dashboard",
#     tags=["Dashboard"]
# )

# app.include_router(
#     inventory.router,
#     prefix="/analytics/inventory",
#     tags=["Inventory Analytics"]
# )

app.include_router(
    assets.router,
    prefix="/analytics/assets",
    tags=["Asset Analytics"]
)

app.include_router(
    work_orders.router,
    prefix="/analytics/work-orders",
    tags=["Work Order Analytics"]
)

# app.include_router(
#     parts.router,
#     prefix="/analytics/parts",
#     tags=["Parts Analytics"]
# )