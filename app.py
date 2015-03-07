from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('<body><h1>Yolo!</h1></body>')

def about_me(request):
    return Response('<body><h1>I am all about that bass.</h1></body>')

def contact_me(request):
    return Response(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title></title>
        </head>
        <body style="color: red;">
            <h1>twitter: @thomaswhyyou</h1>
            you are visiting at: {}
        </body>
        </html>
        """.format(request.domain)
    )

if __name__ == "__main__":
    config = Configurator()

    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')

    config.add_route('about', '/about')
    config.add_view(about_me, route_name='about')

    config.add_route('contact_page', '/contact')
    config.add_view(contact_me, route_name='contact_page')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 5000, app)
    server.serve_forever()
