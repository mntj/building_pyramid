from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello', renderer="../templates/index.html")
def hello_world(request):
    return {
        "monkey": "I'm a test monkey"
    }


@view_config(route_name='about', renderer="../templates/about.html")
def about_me(request):
    return {}


@view_config(route_name='contact_page', renderer="../templates/contact.html")
def contact_me(request):
    return {
        "where": request.domain
    }
