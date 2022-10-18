import os, sys
sys.path.insert(0, '/home/s/danilmmo/danilmmo.beget.tech/coolsite')
sys.path.insert(1, '/home/s/danilmmo/danilmmo.beget.tech/djangoenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'coolsite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()