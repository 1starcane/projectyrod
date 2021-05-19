import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-isdfszcure-i_vi=443#vh6r0g(g_dz2314kdzl*tfae(bs#48z+&+t1hj*'
DEBUG = True
ALLOWED_HOSTS = ['projectyrod.ru']

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'projectyrod',
        'USER': 'yrod',
        'PASSWORD': '5352274',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}