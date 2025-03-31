from fastapi import APIRouter
from com.hc_fast.statements.consolidated import consolidated_router

statements_router = APIRouter()

statements_router.include_router(consolidated_router, prefix="/con")