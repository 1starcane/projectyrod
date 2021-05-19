import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-i_vi=pk3#vh6r0g(g_dzxt@7meoqyq*tfae(bs#48z+&+t1hj*'
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'projectyrod',
        'USER': 'postgres',
        'PASSWORD': '5352274',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
