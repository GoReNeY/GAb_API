from pydantic import BaseSettings, SecretStr, AnyUrl


class Settings(BaseSettings):

    EPIC_GAMES_API_URL: AnyUrl
    EPIC_GAMES_API_HOST: str

    RapidAPI_Key: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()  # type: ignore
