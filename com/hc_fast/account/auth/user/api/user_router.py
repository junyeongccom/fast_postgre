from fastapi import APIRouter, Body, Depends, Response 
from fastapi.responses import JSONResponse
from asyncpg import Connection
from com.hc_fast.account.auth.user.api.user_controller import UserController
from com.hc_fast.account.auth.user.model.user_schema import UserLoginSchema
from com.hc_fast.utils.creational.builder.db_builder import get_db
import traceback
import logging

router = APIRouter()
controller = UserController()
logger = logging.getLogger(__name__)

@router.post("/login")
async def handle_user(
    user_schema: UserLoginSchema = Body(...), 
    db: Connection = Depends(get_db),
    response = Response
):
    logger.info(f"🔐 로그인 요청 받음: 사용자 ID={user_schema.user_id}")
    
    try:
        # ✅ response 전달
        result = await controller.login(user_schema=user_schema, db=db, response = response)
        
        if result.get("status") == "success":
            logger.info(f"🎯 로그인 성공: 사용자 ID={user_schema.user_id}")
        else:
            logger.warning(f"⚠️ 로그인 실패: 사용자 ID={user_schema.user_id}, 이유={result.get('message')}")
            
        return JSONResponse(content=result)
        
    except Exception as e:
        error_msg = f"🔴 로그인 처리 중 예외 발생: {str(e)}"
        logger.error(error_msg)
        logger.error(traceback.format_exc())
        
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": f"로그인 처리 중 서버 오류가 발생했습니다: {str(e)}",
                "user": None
            }
        )
