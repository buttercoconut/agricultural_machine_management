# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.agricultural_machine import router as machine_router
from app.api.maintenance import router as maintenance_router
from app.api.part import router as part_router
from app.api.rental import router as rental_router
from app.api.user import router as user_router

app = FastAPI(title="Agricultural Machine Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(machine_router, prefix="/machines", tags=["machines"])
app.include_router(maintenance_router, prefix="/maintenances", tags=["maintenances"])
app.include_router(part_router, prefix="/parts", tags=["parts"])
app.include_router(rental_router, prefix="/rentals", tags=["rentals"])
app.include_router(user_router, prefix="/users", tags=["users"])
