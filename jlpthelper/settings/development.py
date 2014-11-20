import os

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = 'xejs&+h_@t4qa$8ger2$@(00a3c-#8y^%)@ex0&2rc5r8$-e%n'

DEBUG = TEMPLATE_DEBUG = True

ADMINS = (
    ('Anton', 'antonerjomin@gmail.com'),
    ('Sergey', 'sergey.demenok@gmail.com'),
)

MANAGERS = ADMINS

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jlpthelper.apps.kanji_analyzer',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jlpthelper.urls'

WSGI_APPLICATION = 'jlpthelper.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'assets'),
)

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_PORT = 587

EMAIL_HOST_USER = 'jlpthelper@gmail.com'

EMAIL_HOST_PASSWORD = 'japanesestudy'
