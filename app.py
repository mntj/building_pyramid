from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

# Let's build the simplest web app possible.

if __name__ == "__main__":
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(lambda request: Response('Yolo!'), route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 5000, app)
    server.serve_forever()
