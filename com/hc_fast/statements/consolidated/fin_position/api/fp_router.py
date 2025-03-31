from fastapi import APIRouter
from com.hc_fast.statements.consolidated.fin_position.model.fp_schema import FpSchema
from com.hc_fast.statements.consolidated.fin_position.services.fp_lookup import get_bs_template


router = APIRouter()

@router.get("/bs-template", response_model=list[FpSchema])
async def read_bs_template():
    """
    기본 연결재무상태표 계정과목 템플릿 반환
    """
    return get_bs_template()
