from fastapi import APIRouter, Body
from typing import Annotated

from app.services.Convert_API import Convert_API
from app.utils.translate import translate


utils_router = APIRouter(prefix="/utils", tags=["UTILS_ROUTER"])


@utils_router.post("/translate")
async def translation(body: Annotated[str, Body()]) -> str | None:

    return await translate(body)


@utils_router.post("/convert")
async def convert(body: Annotated[str, Body()]) -> str | None:
    async with Convert_API() as api:
        return await api.convert(body)
