import os

import pytest

from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
