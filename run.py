from aiohttp import web
from app import create_app

app = create_app()

if __name__ == '__main__':
    web.run_app(app, port=8080)