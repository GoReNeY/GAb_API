from fastapi import FastAPI
from app.routes.test import test_router
from app.routes.free_games import free_games_router
from app.routes.database import database_router


app = FastAPI()

for router in [test_router, free_games_router, database_router]:
    app.include_router(router)
