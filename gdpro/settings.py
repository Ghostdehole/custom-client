import os
import sys
from pathlib import Path
from urllib.parse import urlparse


def _is_secret_key_required():
    if len(sys.argv) < 2:
        return True
    command = sys.argv[1]
    safe_commands = {
        'collectstatic',
        'makemigrations',
        'migrate',
        'check',
        'compilemessages',
        'help',
        'version',
        'test',
    }
    return command not in safe_commands

SECRET_KEY = os.environ.get('SECRET_KEY')

if _is_secret_key_required() and not SECRET_KEY:
    raise ValueError(
        "SECRET_KEY is empty."
    )


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
GHUSER = os.environ.get('GHUSER', '').strip()
GENURL = os.environ.get("GENURL", "").strip()
GHBEARER = os.environ.get('GHBEARER', '').strip()
PROTOCOL = os.environ.get("PROTOCOL", 'https')
REPONAME = os.environ.get("REPONAME", 'gdpro')


# --- MEDIA_ROOT ---
MEDIA_ROOT = BASE_DIR / 'media'


# SECURITY WARNING: don't run with debug turned on in production!

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

if GENURL:
    parsed = urlparse(GENURL)
    host = parsed.hostname
    if not host:
        raise ValueError(f"Invalid GENURL: {GENURL}")
    ALLOWED_HOSTS = [host]

    scheme = parsed.scheme or 'https'
    port = f":{parsed.port}" if parsed.port else ""
    auto_origin = f"{scheme}://{host}{port}"
else:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    auto_origin = None

manual_origins = [origin for origin in os.getenv('CSRF_TRUSTED_ORIGINS', '').split() if origin]
CSRF_TRUSTED_ORIGINS = ([auto_origin] if auto_origin else []) + manual_origins


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uigdpro',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'uigdpro.middleware.GlobalMaintenanceErrorMiddleware',

]

ROOT_URLCONF = 'gdpro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gdpro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATA_UPLOAD_MAX_MEMORY_SIZE = None


