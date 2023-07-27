import os
from django.utils.translation import gettext_lazy as _
from pathlib import Path

# import django_heroku
# import dj_database_url
# from decouple import config



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hf2yo5^itx^7x*%@hjm9(fbph&_)i%8rb)$qu0+su+v_p$ex#j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS =  ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'tools.apps.ToolsConfig',
    'account.apps.AccountConfig',
    
    # 'social_django',
    # 'django_extensions',
    
    # tailwind css Django apps
    'tailwind',
    'theme',
    'django_browser_reload',
    
    # for trans
    'rosetta',
    
]
# TAILWIND
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ["127.0.0.1", 'web-production-63c2.up.railway.app']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # for trans
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # for static files in Globale
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    "django_browser_reload.middleware.BrowserReloadMiddleware",    
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.join(BASE_DIR, 'templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'theme.context_processors.theme'
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'T23ADhPx87wKHscyNKx2',
        'HOST': 'containers-us-west-124.railway.app',
        'PORT': '6386',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT ='staticfiles/'
# for static files in Globale
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = 'login_view'

# Email server configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'azizkrayyem7@gmail.com'
EMAIL_HOST_PASSWORD = 'azizkrayyem1234567890@@'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# django_heroku.settings(locals())

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
    # ('ar', _('Arabic')),
    ('tr', _('Türkiye')),
    ('ru', _('Russia')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)