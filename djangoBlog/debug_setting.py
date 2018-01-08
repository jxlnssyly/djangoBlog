# encoding:utf-8
from base_setting import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_blog',
        'USER':'username',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':'5432',
    }
}





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# STATIC_ROOT = '/var/www/djangoBlog/static'
