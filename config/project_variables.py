from decouple import config

APP_HOST = config('HOST')
REDIS_STORAGE_HOST = config('DB_STORAGE_HOST')
REDIS_PORT = config('DB_PORT')
REDIS_STORAGE_PASSWORD = config('DB_STORAGE_PASSWORD')