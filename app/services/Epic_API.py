from app.services.Base_API import BaseAPI
from app.settings import settings

from typing import List, Dict, Any


class EpicAPI(BaseAPI):

    _base_url = settings.EPIC_GAMES_API_URL

    async def get_current_games(self) -> List[Dict[str, Any]]:
        async with self._session.get("/epic-free-games") as responce:
            return await responce.json(content_type="text/html")

    async def get_next_games(self) -> List[Dict[str, Any]]:
        async with self._session.get("/epic-free-games-coming-soon") as responce:
            return await responce.json(content_type="text/html")

    @staticmethod
    def get_headers() -> Dict[str, str]:
        return {
            "X-RapidAPI-Key": settings.RapidAPI_Key.get_secret_value(),
            "X-RapidAPI-Host": settings.EPIC_GAMES_API_HOST
        }
