from pydantic import BaseSettings


class Settings(BaseSettings):
    CHATGPT_KEY: str
    SERVER_IP_ADDRESS: str
    SERVER_PORT: int
    CHATGPT_START_MESSAGE: str = open("../server/chatgpt_start_message.txt", "r").read()
    INFER_URL: str

    class Config:
        env_file = "../server/.env"


settings = Settings()
