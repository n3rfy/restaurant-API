from fastapi import APIRouter

from .cook import router as router_cook
from .waiter import router as router_waiter

router = APIRouter()

router.include_router(router_cook)
router.include_router(router_waiter)
