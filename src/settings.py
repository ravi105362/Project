from starlette.config import Config

config = Config(".env")

LOGGER_FOLDER = config("LOGGER_FOLDER", cast=str, default="src/logs/")
