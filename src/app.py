from .database.database import database, engine, metadata
from .api import router
from .core.exc_class import ExceptionAll

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

app.state.database = database
app.include_router(router)

@app.exception_handler(ExceptionAll)
def validation_exception_handler(request: Request, exc: ExceptionAll):
    return JSONResponse(
        status_code=exc.status_code, 
        content=exc.content
    )

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

