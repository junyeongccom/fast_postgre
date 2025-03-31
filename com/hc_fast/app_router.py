from fastapi import APIRouter
from com.hc_fast.account.account_router import account_router
from com.hc_fast.statements.statements_router import statements_router

router = APIRouter()

router.include_router(account_router, prefix="/account")
router.include_router(statements_router, prefix="/statements")
