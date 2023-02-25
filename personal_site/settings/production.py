from dotenv import load_dotenv
import os
from personal_site.settings import (
    BASE_DIR,
    INSTALLED_APPS,
    MIDDLEWARE,
    ROOT_URLCONF,
    TEMPLATES,
    WSGI_APPLICATION,
    AUTH_PASSWORD_VALIDATORS,
    LANGUAGE_CODE,
    TIME_ZONE,
    USE_I18N,
    USE_L10N,
    USE_TZ,
    STATIC_ROOT,
    STATIC_URL,
    DEFAULT_AUTO_FIELD,
)

load_dotenv()

ALLOWED_HOSTS = ['carterzenke.me', 'www.carterzenke.me']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DJANGO_DB_NAME'],
        'USER': os.environ['DJANGO_DB_USER'],
        'PASSWORD': os.environ['DJANGO_DB_PASS'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT']
    }
}

DEBUG = False

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
