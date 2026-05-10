# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import engine, async_session
from .models.agricultural_machine import Base as MachineBase
from .api.agricultural_machine import router as machine_router

app = FastAPI(title="Agricultural Machine Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(machine_router)

@app.on_event("startup")
async def on_startup():
    # Create tables if they don't exist
    async with engine.begin() as conn:
        await conn.run_sync(MachineBase.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Welcome to the Agricultural Machine Management API"}
