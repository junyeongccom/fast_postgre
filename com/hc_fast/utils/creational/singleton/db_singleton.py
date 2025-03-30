import os

class DBConfigSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConfigSingleton, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD", "BBuCkoCtiSYdAxdxwbDTjKtCjOjlSUyh")
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.port = os.getenv("POSTGRES_PORT", "5432")
        self.database = os.getenv("POSTGRES_DB")
        self.db_url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        print("🔐 POSTGRES_PASSWORD:", os.getenv("POSTGRES_PASSWORD"))
        print("🔐 POSTGRES_USER:", os.getenv("POSTGRES_USER"))
        print("🔐 POSTGRES_HOST:", os.getenv("POSTGRES_HOST"))
        print("🔐 POSTGRES_PORT:", os.getenv("POSTGRES_PORT"))
        print("🔐 POSTGRES_DB:", os.getenv("POSTGRES_DB"))

# ✅ 전역에서 사용할 인스턴스를 이 안에서 생성해둠
db_singleton = DBConfigSingleton()
