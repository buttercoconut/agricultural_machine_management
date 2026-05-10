from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Rental

router = APIRouter(prefix="/rental", tags=["rental"])

rentals: List[Rental] = []

@router.get("/", response_model=List[Rental])
async def read_rentals():
    return rentals

@router.post("/", response_model=Rental)
async def create_rental(r: Rental):
    rentals.append(r)
    return r

@router.get("/{rental_id}", response_model=Rental)
async def read_rental(rental_id: int):
    for r in rentals:
        if r.id == rental_id:
            return r
    raise HTTPException(status_code=404, detail="Rental not found")

@router.put("/{rental_id}", response_model=Rental)
async def update_rental(rental_id: int, updated: Rental):
    for idx, r in enumerate(rentals):
        if r.id == rental_id:
            rentals[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Rental not found")

@router.delete("/{rental_id}")
async def delete_rental(rental_id: int):
    for idx, r in enumerate(rentals):
        if r.id == rental_id:
            rentals.pop(idx)
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Rental not found")
