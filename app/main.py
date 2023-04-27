from fastapi import FastAPI
from app.routes.test import test_router
from app.routes.epic import epic_router


app = FastAPI()

for router in [test_router, epic_router]:
    app.include_router(router)
