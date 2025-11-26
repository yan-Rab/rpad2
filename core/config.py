from pydantic import BaseSettings


class Settings(BaseSettings):
    MODEL_PATH: str = 'logistic_model.pkl'
    API_VERSION: str = 'v1'
    THRESHOLD: float = 0.5

settings = Settings()