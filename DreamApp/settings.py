from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = 'django-insecure-&x$i$r6v&jexlck+f#7n)hgqrmbv+3yk(^(%#pp@m#ui0amx4d'

#

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'True'

ALLOWED_HOSTS = ["dreamapp-hbpq.onrender.com", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ["https://dreamapp-hbpq.onrender.com"]

LOGIN_URL = "userauths:login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #     self installed
    'shop',
    'userauths',
    'cart',
    'crispy_forms',
    'crispy_bootstrap5',
    'search',

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

ROOT_URLCONF = 'DreamApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "cart.context_processor.cart",

            ],
        },
    },
]

WSGI_APPLICATION = 'DreamApp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'DATABASE_URL': 'postgresql://postgres:effE-B1G-a4GD14DAFcgbd1A-g222D5G@postgres.railway.internal:5432/railway',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': 'effE-B1G-a4GD14DAFcgbd1A-g222D5G',
#         'HOST': 'monorail.proxy.rlwy.net',
#         'PORT': 13768,
#     }
# }
#
# DATABASE_URL = config("DATABASE_URL", default="")
# DATABASES["default"] = dj_database_url.config(default=DATABASE_URL, conn_max_age=600)


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

# Static files (CSS, JavaScript, images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files (uploads)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'userauths.User'

JAZZMIN_SETTINGS = {
    # title of the window
    "site_title": "Dreanzz",

    # Title on the brand, and the login screen (19 chars max)
    "site_header": "Dreamzz",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Dreamzz Admin",

    # Custom CSS files for the admin panel

    # Custom JS files for the admin panel

    # Whether to show the UI customizer on admin pages
    "show_ui_builder": True,

    "site_logo": "shop_media/DreamAppFavoicon.png"

    # Whether to cache the menu tree
}

CRISPY_ALLOWED_TEMPLATES_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
