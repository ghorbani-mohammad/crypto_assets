import os
from envparse import env
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = env.bool("DEBUG")
SECRET_KEY = env.str('SECRET_KEY')
ALLOWED_HOSTS = ['crypto.m-gh.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jalali',
    'user',
    'exchange',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crypto_assets.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crypto_assets.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

if not DEBUG:
    MEDIA_URL = "/static/media/"
else:
    MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CELERY
BROKER_URL = "redis://crypto_assets_redis:6379"
CELERY_RESULT_BACKEND = "redis://crypto_assets_redis:6379"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Tehran"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': env.str("POSTGRES_USERNAME"),
        'PASSWORD': env.str("POSTGRES_PASSWORD"),
        'HOST': 'crypto_assets_db',
        'PORT': '5432',
    }
}

AUTH_USER_MODEL = 'user.Profile'


# LOG
log_path = "/var/log/app/"
os.makedirs(os.path.dirname(log_path), exist_ok=True)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'},
    },
    'handlers': {
        'general_log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(log_path, 'logs.log'),
            'formatter': 'standard',
        },
    },
    'loggers': {
        # all modules
        '': {
            'handlers': ['general_log_file'],
            'level': 'INFO',
        },
    },
}
