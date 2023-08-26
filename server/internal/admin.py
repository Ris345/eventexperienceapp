from fastapi import APIRouter

router = APIRouter()

# admin path ops
# shared with other projects in the organization
# can't directly mod and add prefix, dependencies, tags directly to APIRouter
# can do so in main.py


@router.post("/")
async def update_admin():
    return {"message": "admin is setup"}
