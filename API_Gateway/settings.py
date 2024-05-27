import os


class Settings:
    AUTH_SERVICE_URL: str = os.getenv('AUTH_SERVICE_URL', 'http://localhost:8002')
    CALENDAR_SERVICE_URL: str = os.getenv('CALENDAR_SERVICE_URL', 'http://localhost:5000')
    class Config:
        env_file = ".env"


settings = Settings()
