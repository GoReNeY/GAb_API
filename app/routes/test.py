from fastapi import APIRouter

test_router = APIRouter(prefix="/test", tags=["TEST"])


@test_router.get("")
async def test() -> dict:
    return {"message": "hello world"}
