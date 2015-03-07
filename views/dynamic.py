from pyramid.view import view_config


@view_config(route_name='item', renderer="../templates/item.html")
def show_item(request):
    item_id = request.matchdict['item_id']
    return {
        "item_id": item_id
    }
