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
SECRET_KEY = 'hf2yo5^itx^7x*%@hjm9(fbph&_)i%8rb)$qu0+su+v_p$ex#j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS =  ['127.0.0.1', 'web-production-63c2.up.railway.app']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django apps
    'theme.apps.ThemeConfig',
    'tools.apps.ToolsConfig',
    'account.apps.AccountConfig',
    
    # 3rd party libraries
    # 'social_django',
    # 'django_extensions',
    # 'corsheaders',
    
    # tailwind css Django apps
    'tailwind',
    'django_browser_reload',
    
    # for trans
    'rosetta',
    
    'storages'
]

# TAILWIND


TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ["127.0.0.1",]

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

    
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Added by me
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

CSRF_TRUSTED_ORIGINS = ['https://web-production-63c2.up.railway.app']

ROOT_URLCONF = 'mysite.urls'
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# # # Set the HSTS header for 1 year (recommended value)
# SECURE_HSTS_SECONDS = 31536000

# # # Include subdomains in HSTS policy
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# # # Enable HSTS preload
# SECURE_HSTS_PRELOAD = True



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


LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    # ('ar', _('Arabic')),
    ('tr', _('Türkiye')),
    ('ru', _('Russia')),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
else:
    # for static files in Globale
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
STATIC_ROOT ='staticfiles/'



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = 'login_view'

# Email server configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'azizkrayyem7@gmail.com'
EMAIL_HOST_PASSWORD = 'azizkrayyem1234567890@@'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# # s3 BUCKETS CONFIG
# AWS_ACCESS_KEY_ID = ''
# AWS_SECRET_ACCESS_KEY = ''
# AWS_STORAGE_BUCKET_NAME = 'aziz-shop'

# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

'''
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration>
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>DELETE</AllowedMethod>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
'''


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# django_heroku.settings(locals())