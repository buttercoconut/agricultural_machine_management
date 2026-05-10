from fastapi import FastAPI
from .api import agricultural_machine, maintenance, part, rental, user

app = FastAPI(title="Agricultural Machine Management API")

app.include_router(agricultural_machine.router)
app.include_router(maintenance.router)
app.include_router(part.router)
app.include_router(rental.router)
app.include_router(user.router)
