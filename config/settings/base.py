# settings.py

import os, sys
from pathlib import Path
import environ

# Common settings
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
env = environ.Env()

# Read .env file, defaulting to .env if no specific environment is set
env_file = Path(__file__).resolve().parent / '../../.env'  # Default .env file

import os
current_env = os.getenv('DJANGO_ENV', 'development')  # Default to development

# Check environment and load the corresponding .env file
if current_env == 'production':
    env_file = Path(__file__).resolve().parent / '../../.env.production'
elif current_env == 'development':
    env_file = Path(__file__).resolve().parent / '../../.env.development'
elif current_env == 'staging':
    env_file = Path(__file__).resolve().parent / '../../.env.staging'
elif current_env == 'test':
    env_file = Path(__file__).resolve().parent / '../../.env.test'

environ.Env.read_env(env_file)

DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
SECRET_KEY=env("SECRET_KEY")

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',       # Optional; remove if not using Django's admin
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_injector',
    'apps',
    'rest_framework',             # Django Rest Framework
    'rest_framework_mongoengine',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'apps.config',
    'apps.news.config.NewsConfig',      # News app-specific config
    'apps.users.config.UsersConfig', 
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.utils.middleware.CustomExceptionMiddleware'
]

# URL configuration
ROOT_URLCONF = 'config.urls'  # Replace with your project name

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

#AUTH_USER_MODEL = 'users.ApplicationUser'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 
# WSGI application
WSGI_APPLICATION = 'config.wsgi.application'  # Replace with your project name


# MongoDB settings using MongoEngine
from mongoengine import connect

MONGO_DB_NAME = env('MONGO_DB_NAME', default='news_app_db')
MONGO_DB_HOST = env('MONGO_DB_HOST', default='localhost')
MONGO_DB_PORT = env.int('MONGO_DB_PORT', default=27017)

# Establish MongoEngine connection (no need for Django's `DATABASES` setting)
connect(
    db=MONGO_DB_NAME,
    host=MONGO_DB_HOST,
    port=MONGO_DB_PORT
)

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Django Rest Framework settings (optional customizations)
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # Ensures JSON response for API views
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'UNAUTHENTICATED_USER': None,
    'UNAUTHENTICATED_TOKEN': None,
}

AUTHENTICATION_BACKENDS = (
    'apps.users.auth_backend.EmailAuthBackend',  # Add the full path to the EmailAuthBackend class
     'django.contrib.auth.backends.ModelBackend',  # Keep the default backend as a fallback
)

REST_FRAMEWORK['EXCEPTION_HANDLER'] = 'apps.utils.custom_exception_handler2'