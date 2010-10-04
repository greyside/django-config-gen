import os
import sys

sys.stdout = sys.stderr

sys.path.append('/code')
os.environ['DJANGO_SETTINGS_MODULE'] = '{{SETTINGS_MODULE}}'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

