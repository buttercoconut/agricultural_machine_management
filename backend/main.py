# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import (
    agricultural_machine as am_api,
    maintenance as maintenance_api,
    part as part_api,
    rental as rental_api,
    user as user_api,
)

app = FastAPI(title="Agricultural Machine Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(am_api.router, prefix="/api/agricultural-machines", tags=["Agricultural Machines"])
app.include_router(maintenance_api.router, prefix="/api/maintenance", tags=["Maintenance History"])
app.include_router(part_api.router, prefix="/api/parts", tags=["Parts"])
app.include_router(rental_api.router, prefix="/api/rentals", tags=["Rentals"])
app.include_router(user_api.router, prefix="/api/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "Welcome to Agricultural Machine Management API"}
