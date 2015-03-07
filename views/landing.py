from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='hello')
def hello_world(request):
    return Response('<body><h1>Yolo!</h1></body>')


@view_config(route_name='about')
def about_me(request):
    return Response('<body><h1>I am all about that bass.</h1></body>')


@view_config(route_name='contact_page')
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
