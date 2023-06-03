from app.services.Base_API import BaseAPI

from app.models.game import Game

from app.settings import settings

from typing import List, Dict


class Free_Games_API(BaseAPI):

    _base_url = settings.FREE_GAMES_API_URL

    async def get_all_free_games(self) -> List[Game] | None:
        async with self._session.get("/api/giveaways") as responce:
            if responce.status == 201:
                return None
            return await responce.json()

    async def get_free_games_by_platforms(self, platforms: str, type: str) -> List[Game] | None:
        async with self._session.get("/api/filter", params={"platform": platforms,
                                                            "type": type,
                                                            "sort-by": "date"}) as responce:
            if responce.status == 201:
                return None
            return await responce.json()

    @staticmethod
    def get_headers() -> Dict[str, str]:
        return {
            "X-RapidAPI-Key": settings.RapidAPI_Key.get_secret_value(),
            "X-RapidAPI-Host": settings.FREE_GAMES_API_HOST
        }
