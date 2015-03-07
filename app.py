from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from views import landing

if __name__ == "__main__":
    config = Configurator()

    config.add_route('hello', '/')
    config.add_view(landing.hello_world, route_name='hello')

    config.add_route('about', '/about')
    config.add_view(landing.about_me, route_name='about')

    config.add_route('contact_page', '/contact')
    config.add_view(landing.contact_me, route_name='contact_page')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 5000, app)
    server.serve_forever()
