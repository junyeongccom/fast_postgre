from fastapi import APIRouter
from com.hc_fast.statements.consolidated.fin_position.api import fp_router as router

consolidated_router = APIRouter()

consolidated_router.include_router(router, prefix="/fp")