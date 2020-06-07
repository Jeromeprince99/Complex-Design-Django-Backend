from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from complex_design_backend.consumers import wsconsumer
'''
from channels.staticfiles import StaticFilesConsumer
from complex_design_backend.consumers import wsconsumer

channel_routing = {
    # This makes Django serve static files from settings.STATIC_URL, similar
    # to django.views.static.serve. This isn't ideal (not exactly production
    # quality) but it works for a minimal example.
    'http.request': StaticFilesConsumer(),

    # Wire up websocket channels to our consumers:
    'websocket.connect':  wsconsumer.websocket_connect,
    'websocket.receive':  wsconsumer.websocket_receive,
    'websocket.disconnect': wsconsumer.websocket_disconnect,
}'''

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket':AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url('wsnotif',wsconsumer)
                ]
            )
        )
    )
})