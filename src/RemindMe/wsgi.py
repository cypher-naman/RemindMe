"""
WSGI config for RemindMe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
from django.core.wsgi import get_wsgi_application

from base.services import _set_django_settings_module

_set_django_settings_module()

application = get_wsgi_application()
