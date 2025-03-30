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
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.port = os.getenv("POSTGRES_PORT", "5432")
        self.database = os.getenv("POSTGRES_DB")
        self.db_url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

# ✅ 전역에서 사용할 인스턴스를 이 안에서 생성해둠
db_singleton = DBConfigSingleton()
