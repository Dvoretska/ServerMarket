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
#
# DATABASES = {
#     "default": {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd16bsh6sm0938k',
#         'USER': 'uustiofiinxyyy',
#         'PASSWORD': '08097c8be847c943d0b0b84da16715c1b319bbc649e584e9241c8c17ce9ff278',
#         'HOST': 'ec2-54-243-63-13.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
    }
}