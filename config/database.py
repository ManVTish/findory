from redis_om import get_redis_connection

redis = get_redis_connection(
    host = REDIS_STORAGE_HOST,
    port = REDIS_PORT,
    password = REDIS_STORAGE_PASSWORD,
    decode_responses = True)
