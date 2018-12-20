

import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gjr+ijmr(8i&vf=u=r*e+od6h1!iudymhg--+qp_s=vh%)xaq$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog_db',
        'USER': 'ayp',
        'PASSWORD': 'a18803100108',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
'''

#发送邮件设置
# https://docs.djangoproject.com/en/2.0/ref/settings/#email
# https://docs.djangoproject.com/en/2.0/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '850016457@qq.com'
EMAIL_HOST_PASSWORD = 'funlfxilavtdbefh'  # 授权码
EMAIL_SUBJECT_PREFIX = '[安亚鹏的博客]'
EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)