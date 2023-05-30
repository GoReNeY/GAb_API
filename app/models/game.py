from pydantic import BaseModel, AnyUrl, Field


class Game(BaseModel):

    id: int

    price: str = Field(alias="worth")

    title: str
    description: str

    image: str

    published_date: str
    end_date: str

    platforms: str

    open_giveaway: AnyUrl
