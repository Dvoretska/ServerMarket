try:
    from market.settings import *
except ImportError:
    pass

DEBUG = True
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'market',
        'USER': 'anton',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
    }
}