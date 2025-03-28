import asyncpg
from contextlib import asynccontextmanager
from com.hc_fast.utils.creational.singleton.db_singleton import db_singleton


class DatabaseBuilder:
    _pool = None  # 전역 싱글톤 풀

    def __init__(self):
        self.database_url = db_singleton.db_url
        self.min_size = 1
        self.max_size = 10
        self.timeout = 60

    def set_pool_size(self, min_size: int = 1, max_size: int = 10):
        self.min_size = min_size
        self.max_size = max_size
        return self

    def set_timeout(self, timeout: int = 60):
        self.timeout = timeout
        return self

    async def build(self):
        if not self.database_url:
            raise ValueError("❌ Database URL이 설정되지 않았습니다.")

        if DatabaseBuilder._pool is None:
            print(f"🚀 커넥션 풀 생성 중... {self.database_url}")
            DatabaseBuilder._pool = await asyncpg.create_pool(
                dsn=self.database_url,
                min_size=self.min_size,
                max_size=self.max_size,
                timeout=self.timeout
            )
            print("✅ 커넥션 풀 생성 완료")
        else:
            print("ℹ️ 이미 커넥션 풀이 초기화되어 있어 재사용됩니다.")

        return AsyncDatabase(DatabaseBuilder._pool)

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            raise Exception("❌ 커넥션 풀이 아직 초기화되지 않았습니다.")
        return cls._pool


# 내부에서 fetch/execute 등을 제공하는 래퍼 클래스
class AsyncDatabase:
    def __init__(self, pool):
        self.pool = pool

    @asynccontextmanager
    async def get_db(self):
        conn = await self.pool.acquire()
        try:
            yield conn
        finally:
            await self.pool.release(conn)

    async def fetch(self, query, *args):
        async with self.get_db() as conn:
            return await conn.fetch(query, *args)
    
    async def execute(self, query, *args):
        async with self.get_db() as conn:
            return await conn.execute(query, *args)

    async def close(self):
        await self.pool.close()

# 의존성 주입용 함수 (FastAPI의 Depends에서 사용)
async def get_db():
    # 글로벌 db 인스턴스가 없으면 생성
    if not hasattr(get_db, '_db_instance') or get_db._db_instance is None:
        builder = DatabaseBuilder()
        get_db._db_instance = await builder.build()
    
    # 데이터베이스 인스턴스 반환
    return get_db._db_instance
