from pydantic import BaseSettings, SecretStr, AnyUrl


class Settings(BaseSettings):

    FREE_GAMES_API_URL: AnyUrl
    FREE_GAMES_API_HOST: str
    PRICING_COUNTRY: str

    RapidAPI_Key: SecretStr

    BOT_TOKEN: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()  # type: ignore
