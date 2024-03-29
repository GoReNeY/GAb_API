from fastapi import APIRouter
from typing import List

from app.services.Free_Games_API import Free_Games_API
from app.models.game import Game


free_games_router = APIRouter(prefix="/free_games", tags=["FREE_GAMES"])


class Free_Games_Router:

    @staticmethod
    @free_games_router.get("/all")
    async def all_free_games() -> List[Game] | None:

        async with Free_Games_API() as api:
            return await api.get_all_free_games()

    @staticmethod
    @free_games_router.get("/giveaway_p")
    async def free_games_by_platform(platform: str, type: str) -> List[Game] | None:
        async with Free_Games_API() as api:
            return await api.get_free_games_by_platforms(platform, type)
