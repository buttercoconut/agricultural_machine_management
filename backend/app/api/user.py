from fastapi import APIRouter, HTTPException
from typing import List
from ..models import User

router = APIRouter(prefix="/user", tags=["user"])

users: List[User] = []

@router.get("/", response_model=List[User])
async def read_users():
    return users

@router.post("/", response_model=User)
async def create_user(u: User):
    users.append(u)
    return u

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    for u in users:
        if u.id == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, updated: User):
    for idx, u in enumerate(users):
        if u.id == user_id:
            users[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    for idx, u in enumerate(users):
        if u.id == user_id:
            users.pop(idx)
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="User not found")
