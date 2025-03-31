from fastapi import APIRouter
from com.hc_fast.statements.consolidated.fin_position.api.fp_router import router as fp_router

consolidated_router = APIRouter()

consolidated_router.include_router(fp_router, prefix="/fp")