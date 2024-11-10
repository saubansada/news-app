# config/production.py
from .base import *

# Production-specific settings
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
