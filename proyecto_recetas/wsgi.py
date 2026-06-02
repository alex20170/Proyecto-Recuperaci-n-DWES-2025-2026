"""
Configuración WSGI para el proyecto proyecto_recetas.

Expone el llamable WSGI como una variable a nivel de módulo denominada ``application``.

Para más información sobre este archivo, ver
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_recetas.settings')

application = get_wsgi_application()
