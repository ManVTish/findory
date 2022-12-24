from decouple import config

# APP domain
APP_HOST = config('HOST')

# Redis DB
REDIS_STORAGE_HOST = config('DB_STORAGE_HOST')
REDIS_PORT = config('DB_PORT')
REDIS_STORAGE_PASSWORD = config('DB_STORAGE_PASSWORD')