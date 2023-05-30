import json

from fastapi import APIRouter, Request, Body
from typing import Dict, Annotated

from app.utils.database import Database
from app.settings import settings


database_router = APIRouter(prefix="/database", tags=["DATABASE"])


@database_router.get("/platforms")
async def get_user_platforms(user_id: int, request: Request) -> Dict:

    if not request.headers.get("Autorization") == settings.BOT_TOKEN.get_secret_value():
        return {"Access Denied": "Token is missing or incorrect"}

    with Database() as db:
        db.execute("SELECT user_platforms FROM platforms WHERE user_id = ?", (user_id,))
        user_platforms = db.fetchone()

        if user_platforms:
            return json.loads(*user_platforms)

    return {"not_in_db": True}


@database_router.put("/platforms")
async def set_user_platforms(user_id: int, request: Request, body: Annotated[str, Body()]) -> Dict:

    if not request.headers.get("Autorization") == settings.BOT_TOKEN.get_secret_value():
        return {"Access Denied": "Token is missing or incorrect"}

    with Database() as db:
        db.execute("""INSERT INTO platforms (user_id, user_platforms)
                      VALUES (?,?)
                      ON CONFLICT(user_id) DO
                      UPDATE SET user_platforms = ?;""", (user_id, body, body))
        db.commit()

    return {}
