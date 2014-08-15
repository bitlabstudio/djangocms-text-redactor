"""Settings that need to be set in order to run the tests."""
import os
import logging

DEBUG = True

logging.getLogger("factory").setLevel(logging.WARN)

SITE_ID = 1

LANGUAGES = [
    ('en', 'English'),
]

APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'djangocms_text_redactor.tests.urls'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(APP_ROOT, '../app_static')
MEDIA_ROOT = os.path.join(APP_ROOT, '../app_media')
STATICFILES_DIRS = (
    os.path.join(APP_ROOT, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(APP_ROOT, 'tests/test_app/templates'),
)

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.join(APP_ROOT, 'tests/coverage'))
COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_nose',
    'cms',
    'mptt',
    'menus',
    'sekizai',
]

INTERNAL_APPS = [
    'djangocms_text_redactor',
    'djangocms_text_redactor.tests.test_app',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS
COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS

CMS_TEMPLATES = (
    ('default.html', 'Default template'),
)
CMS_MODERATOR = False
CMS_PERMISSION = True
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
]

SECRET_KEY = 'foobar'
