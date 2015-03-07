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
