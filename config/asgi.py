import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import websockets.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websockets.routing.websocket_urlpatterns
        )
    ),
})

if settings.DEBUG:
    from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
    application = ASGIStaticFilesHandler(application)
