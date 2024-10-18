"""
ASGI config for estimation_in_earthquake_earlywarning.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estimation_in_earthquake_earlywarning.settings')

application = get_asgi_application()
