import os, sys

path = '/usr/local/django'

if path not in sys.path:
	sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'gallery.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
