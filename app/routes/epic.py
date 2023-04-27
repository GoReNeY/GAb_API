from fastapi import APIRouter
from app.services.Epic_API import EpicAPI

from typing import List, Dict, Any

epic_router = APIRouter(prefix="/epic_free_games", tags=["EPIC_FREE_GAMES"])


@epic_router.get("/current")
async def current_games() -> List[Dict[str, Any]]:
    async with EpicAPI() as api:
        return await api.get_current_games()


@epic_router.get("/coming_soon")
async def next_games() -> List[Dict[str, Any]]:
    async with EpicAPI() as api:
        return await api.get_next_games()
