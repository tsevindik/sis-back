import os
import datetime

import environ

env = environ.Env()
env.read_env('.env')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='!(+akxq6q0c38can89@(#ga$b9jx5cs*y(k+hv0_zd1wyy#qt=')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=False)

# Default Django apps:
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
)


THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
    'cities',
    'django_jenkins',
)

PROJECT_APPS = (
    'utils',

    'apps.course.course',
    'apps.course.assignment',
    'apps.course.attendance',
    'apps.course.demand',
    'apps.course.grade',
    'apps.course.pool',
    'apps.course.section',

    'apps.finance.account',
    'apps.finance.fee',
    'apps.finance.transaction',

    'apps.institute.institute',
    'apps.institute.exchange',
    'apps.institute.schedule',
    'apps.institute.unit',

    'apps.other.announce',
    'apps.other.formal',
    'apps.other.registry',

    'apps.program.program',
    'apps.program.curriculum',
    'apps.program.major',
    'apps.program.minor',

    'apps.property.facility',
    'apps.property.inventory',

    'apps.user.user',
    'apps.user.instructor',
    'apps.user.staff',
    'apps.user.student',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_flake8',
    'django_jenkins.tasks.run_sloccount',
)

JWT_AUTH = {
    'JWT_PAYLOAD_HANDLER': 'apps.user.user.jwt.jwt_payload_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=3),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apps.urls'

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env("DATABASE_NAME", default="sisdb"),
        'USER': env("DATABASE_USER", default="sis"),
        'PASSWORD': env("DATABASE_PASSWORD", default="123456"),
        'HOST': env("DATABASE_HOST", default="localhost"),
        'PORT': env("DATABASE_PORT", default="5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'user.User'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

CITIES_LOCALES = ['en', 'tr', 'LANGUAGES']

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
