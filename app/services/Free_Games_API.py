from app.services.Base_API import BaseAPI
from app.models.game import Game
from app.settings import settings

from typing import List, Dict


class Free_Games_API(BaseAPI):

    _base_url = settings.FREE_GAMES_API_URL

    async def get_all_free_games(self) -> List[Game]:
        async with self._session.get("/api/giveaways") as responce:
            return await responce.json()

    async def get_free_games_by_platform(self, platform: str) -> List[Game]:
        async with self._session.get("/api/giveaways", params={"platform": platform}) as responce:
            return await responce.json()

    @staticmethod
    def get_headers() -> Dict[str, str]:
        return {
            "X-RapidAPI-Key": settings.RapidAPI_Key.get_secret_value(),
            "X-RapidAPI-Host": settings.FREE_GAMES_API_HOST
        }
