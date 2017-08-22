"""
WSGI config for daymdata project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import sys
import os
sys.path.append('/Users/zzh/anaconda/lib/python2.7/site-packages')
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "daymdata.settings")

application = get_wsgi_application()
