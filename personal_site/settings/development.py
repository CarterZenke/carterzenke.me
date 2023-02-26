from dotenv import load_dotenv
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
    MEDIA_ROOT,
    MEDIA_URL,
    DEFAULT_AUTO_FIELD,
)

load_dotenv()

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEBUG = True

SECRET_KEY = "django-dev-a3ZqqL!7poXk_isvJEPPKs_zXHVEGei!"
