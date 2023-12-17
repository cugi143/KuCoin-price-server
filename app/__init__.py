from aiohttp import web
from app.routes.price_routes import setup_price_routes
from app.middleware.request_logger import request_logger_middleware
from config import DEBUG

def create_app():
    """
    Create the application and add routes and middleware.
    :return: aiohttp.web.Application instance.
    """
    app = web.Application()
    app['debug'] = DEBUG

    if app['debug']:
        app.middlewares.append(request_logger_middleware)

    setup_price_routes(app)  # Add other route setups as needed
    return app