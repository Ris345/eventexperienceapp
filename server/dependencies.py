from typing import Annotated
from fastapi import Header, HTTPException


# invented header for the purpose of dependency implementation
async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-token header invalid")


async def get_query_tolen(token: str):
    if token != "user":
        raise HTTPException(status_code=400, detail="No user-token provided")
