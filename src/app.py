from .database.database import database, engine, metadata
from .api import router

from fastapi import FastAPI

app = FastAPI()

app.state.database = database
app.include_router(router)

@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    metadata.create_all(engine)
    if not database_.is_connected:
        await database_.connect()

@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

