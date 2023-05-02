from fastapi import APIRouter

from app.services.Epic_API import EpicAPI
from app.models.game import Game

from typing import List


epic_router = APIRouter(prefix="/epic_free_games", tags=["EPIC_FREE_GAMES"])


@epic_router.get("/current")
async def current_games() -> List[Game]:
    async with EpicAPI() as api:
        return await api.get_current_games()


@epic_router.get("/coming_soon")
async def next_games() -> List[Game]:
    async with EpicAPI() as api:
        return await api.get_next_games()
