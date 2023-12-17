from app.controllers.price_controller import get_price, get_price_history, delete_price_history

def setup_price_routes(app):
    """
    Setup routes for the price controller.
    The price/history route has to come before the price/{currency} route, because otherwise the latter would match the former.
    """
    app.router.add_get('/price/history', get_price_history)
    app.router.add_get('/price/{currency}', get_price)
    app.router.add_delete('/price/history', delete_price_history)