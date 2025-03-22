import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Static Files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# For Development (local use)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# For Production (Deployment)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media Files (if needed)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security Settings for Deployment
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = ["*"]  # Replace '*' with your domain if applicable

# Ensure Django serves static files
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
