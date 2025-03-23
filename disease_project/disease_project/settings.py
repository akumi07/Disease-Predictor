import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'prediction',
    'rest_framework',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Make sure you have a 'templates' folder
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


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # REQUIRED
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # REQUIRED
    'django.contrib.messages.middleware.MessageMiddleware',  # REQUIRED
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Static Files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# For Development (local use)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# For Production (Deployment)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media Files (if needed)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ROOT_URLCONF = 'disease_project.urls'


# Security Settings for Deployment
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ["*"]  # Replace '*' with your domain if applicable
SECRET_KEY = 'epTiKOky3HaI0wsz-LdAjuHGy7HrGD5ijQqYmuhkq7U3nJOMAU2vUwLiWJmPEZ2lIig'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use the correct database engine
        'NAME': BASE_DIR / "db.sqlite3",  # Database file path
    }
}


# Ensure Django serves static files
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'