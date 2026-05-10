# app/api/rental.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from app.models.rental import Rental
from app.schemas.rental import RentalCreate, RentalUpdate, Rental
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Rental, status_code=status.HTTP_201_CREATED)
async def create_rental(rental: RentalCreate, db: AsyncSession = Depends(get_db)):
    # Calculate total cost
    days = (rental.end_date - rental.start_date).days + 1
    total_cost = days * rental.daily_rate
    db_rental = Rental(**rental.dict(), total_cost=total_cost)
    db.add(db_rental)
    try:
        await db.commit()
        await db.refresh(db_rental)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Rental conflict")
    return db_rental

@router.get("/", response_model=list[Rental])
async def read_rentals(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Rental).offset(skip).limit(limit))
    rentals = result.scalars().all()
    return rentals

@router.get("/{rental_id}", response_model=Rental)
async def read_rental(rental_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Rental).where(Rental.id == rental_id))
    rental = result.scalar_one_or_none()
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental

@router.put("/{rental_id}", response_model=Rental)
async def update_rental(rental_id: int, rental_update: RentalUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Rental).where(Rental.id == rental_id))
    rental = result.scalar_one_or_none()
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    for key, value in rental_update.dict(exclude_unset=True).items():
        setattr(rental, key, value)
    # Recalculate total cost if dates or rate changed
    if "start_date" in rental_update.dict(exclude_unset=True) or "end_date" in rental_update.dict(exclude_unset=True) or "daily_rate" in rental_update.dict(exclude_unset=True):
        days = (rental.end_date - rental.start_date).days + 1
        rental.total_cost = days * rental.daily_rate
    await db.commit()
    await db.refresh(rental)
    return rental

@router.delete("/{rental_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rental(rental_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Rental).where(Rental.id == rental_id))
    rental = result.scalar_one_or_none()
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    await db.delete(rental)
    await db.commit()
    return None
