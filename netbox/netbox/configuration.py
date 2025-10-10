"""
NetBox Configuration
All sensitive data is read from environment variables.
"""
import os
import sys

#########################
#   Required settings   #
#########################

# Allowed hosts - comma-separated list
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# PostgreSQL database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'netbox'),
        'USER': os.environ.get('POSTGRES_USER', 'netbox'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        'CONN_MAX_AGE': int(os.environ.get('DB_CONN_MAX_AGE', '300')),
    }
}

# Redis database settings
REDIS = {
    'tasks': {
        'HOST': os.environ.get('REDIS_HOST', 'localhost'),
        'PORT': int(os.environ.get('REDIS_PORT', '6379')),
        'USERNAME': os.environ.get('REDIS_USERNAME', ''),
        'PASSWORD': os.environ.get('REDIS_PASSWORD', ''),
        'DATABASE': int(os.environ.get('REDIS_DATABASE', '0')),
        'SSL': os.environ.get('REDIS_SSL', 'False').lower() == 'true',
    },
    'caching': {
        'HOST': os.environ.get('REDIS_CACHE_HOST', os.environ.get('REDIS_HOST', 'localhost')),
        'PORT': int(os.environ.get('REDIS_CACHE_PORT', os.environ.get('REDIS_PORT', '6379'))),
        'USERNAME': os.environ.get('REDIS_CACHE_USERNAME', os.environ.get('REDIS_USERNAME', '')),
        'PASSWORD': os.environ.get('REDIS_CACHE_PASSWORD', os.environ.get('REDIS_PASSWORD', '')),
        'DATABASE': int(os.environ.get('REDIS_CACHE_DATABASE', '1')),
        'SSL': os.environ.get('REDIS_CACHE_SSL', os.environ.get('REDIS_SSL', 'False')).lower() == 'true',
    }
}

# Secret key for cryptographic signing
# SECURITY WARNING: This must be set to a random string in production!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# Validate SECRET_KEY in production
if not SECRET_KEY:
    raise ValueError(
        "SECRET_KEY environment variable is required. "
        "Generate one using: python netbox/generate_secret_key.py"
    )
if SECRET_KEY == 'development-secret-key-change-in-production':
    print("WARNING: Using default SECRET_KEY. This is insecure for production!", file=sys.stderr)

#########################
#   Optional settings   #
#########################

# Debug mode - should be False in production
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Developer mode - enables additional features for development
DEVELOPER = os.environ.get('DEVELOPER', 'False').lower() == 'true'

# Require login for all views
LOGIN_REQUIRED = os.environ.get('LOGIN_REQUIRED', 'True').lower() == 'true'

# GraphQL API
GRAPHQL_ENABLED = os.environ.get('GRAPHQL_ENABLED', 'True').lower() == 'true'

# Prometheus metrics
METRICS_ENABLED = os.environ.get('METRICS_ENABLED', 'False').lower() == 'true'

# Base URL path (if NetBox is hosted under a subdirectory)
BASE_PATH = os.environ.get('BASE_PATH', '')

# Timezone
TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

# Default language
DEFAULT_LANGUAGE = os.environ.get('DEFAULT_LANGUAGE', 'en-us')

# CORS settings
CORS_ORIGIN_ALLOW_ALL = os.environ.get('CORS_ORIGIN_ALLOW_ALL', 'False').lower() == 'true'
CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST', '').split(',') if os.environ.get('CORS_ORIGIN_WHITELIST') else []

# Internal IPs for debug toolbar
INTERNAL_IPS = ('127.0.0.1', '::1')

# Enable installed plugins
# You can either:
# 1. Set PLUGINS env var (comma-separated): PLUGINS=plugin1,plugin2
# 2. Hardcode below by uncommenting and adding plugin names
PLUGINS = os.environ.get('PLUGINS', '').split(',') if os.environ.get('PLUGINS') else []
# PLUGINS = ['netbox_topology_views', 'netbox_secrets']  # Hardcoded example

# Plugin configuration (optional)
# PLUGINS_CONFIG = {
#     'netbox_topology_views': {
#         'device_ext_page': 'right',
#     },
# }

# Remote authentication
REMOTE_AUTH_ENABLED = os.environ.get('REMOTE_AUTH_ENABLED', 'False').lower() == 'true'
REMOTE_AUTH_BACKEND = os.environ.get('REMOTE_AUTH_BACKEND', 'netbox.authentication.RemoteUserBackend')
REMOTE_AUTH_HEADER = os.environ.get('REMOTE_AUTH_HEADER', 'HTTP_REMOTE_USER')
REMOTE_AUTH_AUTO_CREATE_USER = os.environ.get('REMOTE_AUTH_AUTO_CREATE_USER', 'True').lower() == 'true'

# Session configuration
SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME', 'sessionid')
CSRF_COOKIE_NAME = os.environ.get('CSRF_COOKIE_NAME', 'csrftoken')

# Email configuration
EMAIL = {
    'SERVER': os.environ.get('EMAIL_SERVER', 'localhost'),
    'PORT': int(os.environ.get('EMAIL_PORT', '25')),
    'USERNAME': os.environ.get('EMAIL_USERNAME', ''),
    'PASSWORD': os.environ.get('EMAIL_PASSWORD', ''),
    'USE_SSL': os.environ.get('EMAIL_USE_SSL', 'False').lower() == 'true',
    'USE_TLS': os.environ.get('EMAIL_USE_TLS', 'False').lower() == 'true',
    'TIMEOUT': int(os.environ.get('EMAIL_TIMEOUT', '10')),
    'FROM_EMAIL': os.environ.get('EMAIL_FROM', ''),
}

# Development banners (only shown when DEBUG=True)
if DEBUG:
    BANNER_TOP = os.environ.get('BANNER_TOP',
        '<strong style="color: #28a745;">🛠 DEVELOPMENT ENVIRONMENT</strong> - This is a development instance of NetBox')
    BANNER_LOGIN = os.environ.get('BANNER_LOGIN',
        'Development Instance - Default credentials: admin/admin')