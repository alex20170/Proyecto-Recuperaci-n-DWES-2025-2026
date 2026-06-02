"""
Configuración ASGI para el proyecto proyecto_recetas.

Expone el llamable ASGI como una variable a nivel de módulo denominada ``application``.

Para más información sobre este archivo, ver
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_recetas.settings')

application = get_asgi_application()
