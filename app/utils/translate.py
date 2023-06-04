from googletrans import Translator

from app.settings import settings

translator = Translator()


async def translate(text: str) -> str:

    return translator.translate(text, settings.LANGUAGE).text  # type: ignore
