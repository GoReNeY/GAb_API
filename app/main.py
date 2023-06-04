from fastapi import FastAPI
from app.routes.free_games import free_games_router
from app.routes.database import database_router
from app.routes.util_routes import utils_router


app = FastAPI()

for router in [free_games_router, database_router, utils_router]:
    app.include_router(router)
