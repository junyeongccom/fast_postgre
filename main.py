from asyncpg import Connection
from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from com.hc_fast.app_router import router as app_router
from fastapi.middleware.cors import CORSMiddleware  
from com.hc_fast.utils.creational.builder.db_builder import get_db
from dotenv import load_dotenv

load_dotenv()

# ✅ FastAPI 애플리케이션 생성
app = FastAPI()
# ✅ CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 모든 도메인에서 요청 허용 (보안상 필요하면 특정 도메인만 허용)
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
