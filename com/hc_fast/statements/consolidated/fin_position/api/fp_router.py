from fastapi import APIRouter
from com.hc_fast.statements.consolidated.fin_position.model.fp_schema import FpSchema
from com.hc_fast.statements.consolidated.fin_position.services import get_fp_service


router = APIRouter()

@router.get("/get", response_model=list[FpSchema])
async def get_fin_position():
    """
    기본 연결재무상태표 계정과목 템플릿 반환
    """
    return get_fp_service()
