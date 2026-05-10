# app/api/part.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from app.models.part import Part
from app.schemas.part import PartCreate, PartUpdate, Part
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Part, status_code=status.HTTP_201_CREATED)
async def create_part(part: PartCreate, db: AsyncSession = Depends(get_db)):
    db_part = Part(**part.dict())
    db.add(db_part)
    try:
        await db.commit()
        await db.refresh(db_part)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Part already exists")
    return db_part

@router.get("/", response_model=list[Part])
async def read_parts(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Part).offset(skip).limit(limit))
    parts = result.scalars().all()
    return parts

@router.get("/{part_id}", response_model=Part)
async def read_part(part_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Part).where(Part.id == part_id))
    part = result.scalar_one_or_none()
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part

@router.put("/{part_id}", response_model=Part)
async def update_part(part_id: int, part_update: PartUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Part).where(Part.id == part_id))
    part = result.scalar_one_or_none()
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    for key, value in part_update.dict(exclude_unset=True).items():
        setattr(part, key, value)
    await db.commit()
    await db.refresh(part)
    return part

@router.delete("/{part_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_part(part_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Part).where(Part.id == part_id))
    part = result.scalar_one_or_none()
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    await db.delete(part)
    await db.commit()
    return None
