#!/usr/bin/env python
import os, sys
from . import settings
from django.core.management import call_command
import django

os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % settings.PROJECT_MODULE
sys.path.insert(0, settings.PROJECT_PARENT_DIR)

def runtests():
    django.setup()
    call_command('test', 'django_config_gen')
    sys.exit()

if __name__ == '__main__':
    runtests()
