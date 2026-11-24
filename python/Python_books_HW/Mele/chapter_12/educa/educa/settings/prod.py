from .base import *
from decouple import config

DEBUG = False

ADMINS = [
    ('Ilya V.', 'email@mydomain.com'),
]

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': config('POSTGRES_DB'),
    'USER': config('POSTGRES_USER'),
    'PASSWORD': config('POSTGRES_PASSWORD'),
    'HOST': 'db',
    'PORT': 5432,
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

CSRF_COOCKIE_SECURE = True
SESSION_COOCKIE_SECURE = True
SECURE_SSL_REDIRECT = True