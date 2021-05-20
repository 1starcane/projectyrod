import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-i421zcure-i_vi=443#asdf1dz2314kdzlszht5e(bs#48z+5&+t1hj*'
DEBUG = True
ALLOWED_HOSTS = [127.0.0.1]

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]


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