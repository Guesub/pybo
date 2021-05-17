"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(arc*4=$xr+73mg$f7+jzj2vk9v^pg78+@=ve1mme-va6b2_i&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['13.125.185.206']


# Application definition

INSTALLED_APPS = [
    #installed app에 pybo apps.py 의 PyboConfig 클라스가 추가되지 않으면 pybo앱을 인식 하지 못하고 데이터베이스작업도 불가
    'pybo.apps.PyboConfig', 
    'common.apps.CommonConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/'

#로깅 설정
LOGGING={
    'version' : 1,
    'disable_existing_loggers' : False,
    'filters':{
        'require_debug_false':{
            '()' :'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true':{
            '()' :'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters':{
        'django.server':{
            '()' : 'django.utils.log.ServerFormatter',
            'format' : '[{server_time}] {message}',
            'style' : '{',
        },
        'standard' :{
            'format' : '%(asctime)s [%(levelname)s] %(name)s : %(message)s'
        }
    },
    'handlers' :{
        'console':{
            'level' : 'INFO',
            'filters' : ['require_debug_true'],
            'class' : 'logging.StreamHandler',
        },
        'django.server':{
            'level' : 'INFO',
            'class' : 'logging.StreamHandler',
            'formatter' : 'django.server',
        },
        'mail_admins':{
            'level' : 'ERROR',
            'filters' : ['require_debug_false'],
            'class' : 'django.utils.log.AdminEmailHandler'
        },
        'file':{
            'level' : 'INFO',
            'filters' : ['require_debug_false'],
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename' : BASE_DIR / 'logs/mysite.log',
            'maxBytes' : 1024*1024*5, # 5MB
            'backupCount' : 5,
            'formatter' : 'standard'
        }
    },
    'loggers': {
        'django':{
            'handlers' : ['console', 'mail_admins', 'file'],
            'level' : 'INFO',
        },
        'django.server': {
            'handlers' : ['django.server'],
            'level' : 'INFO',
            'propagate' : False
        },
    }
}