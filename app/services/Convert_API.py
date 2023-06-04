from app.services.Base_API import BaseAPI

from app.settings import settings


class Convert_API(BaseAPI):

    _base_url = settings.CURRENCY_API

    async def convert(self, cost: str) -> str | None:
        async with self._session.get("/NBUStatService/v1/statdirectory/exchange?json&valcode=USD",
                                     params={"json": 1,
                                             "valcode": "USD"}) as responce:

            rate = (await responce.json())[0]["rate"]

            if cost == "N/A" or cost.endswith(" грн."):
                return cost

            converted_cost: str = str(round(float(cost.strip("$")) * rate, 2)) + " грн."

        return converted_cost
