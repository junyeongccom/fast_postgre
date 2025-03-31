import os
from asyncpg import Connection
from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from com.hc_fast.app_router import router as app_router
from fastapi.middleware.cors import CORSMiddleware  
from com.hc_fast.utils.creational.builder.db_builder import get_db
from com.hc_fast.utils.creational.builder.redis_builder import redis_client
import logging

from com.hc_fast.utils.creational.singleton.redis_singleton import REDIS_URL

print("🔥 main.py started")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)


origins = [
    "http://localhost:3000",  # ✅ 프론트엔드 도메인 정확히 명시
    "https://www.junyeongc.com"
]

# ✅ FastAPI 애플리케이션 생성
app = FastAPI()
# ✅ CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 🔥 특정 도메인에서 요청 허용 (보안상 필요하면 특정 도메인만 허용)
    allow_credentials=True,
    allow_methods=["*"],  # ✅ 모든 HTTP 메서드 허용 (POST, OPTIONS 등)
    allow_headers=["*"],  # ✅ 모든 헤더 허용
)

# ✅ 라우터 등록
app.include_router(app_router, prefix="/api")

# ✅ 루트 경로
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <body>
            <h1>🚀 FastAPI 테스트 서버 실행 중!</h1>
        </body>
    </html>
    """
# ✅ DB 연결 테스트용 엔드포인트
@app.get("/health/db")
async def test_db_connection(db : Connection = Depends(get_db)):
    try:
        result = await db.fetch("SELECT 1;")
        return {"db_connection": True, "result": result}
    except Exception as e:
        return {"db_connection": False, "error": str(e)}

@app.get("/health/redis")
def ping_redis():
    redis_client.set("ping", "pong", ex=10)
    print("🔗 Redis URL:", REDIS_URL)
    return {"message": redis_client.get("ping")}

if __name__ == "__main__":

    port = int(os.getenv("PORT", 8000))  # Railway가 PORT 주입함. 없으면 기본값 8000
    uvicorn.run("main:app", host="0.0.0.0", port=port)