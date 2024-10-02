from fastapi import FastAPI

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from api.cat_router import router as cat_router

from redis import asyncio as aioredis
#from fastapi_cache import FastAPICache
#from fastapi_cache.backends.redis import RedisBackend

import uvicorn

#@asynccontextmanager
#async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    #redis = aioredis.from_url("redis://localhost")
    #FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    #yield


app = FastAPI(
    title="EDWeissTrainingHub",
    #lifespan=lifespan
)

app.include_router(cat_router)


uvicorn.run(app)