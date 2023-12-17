
async def request_logger_middleware(app, handler):
    """
    Middleware decorator that logs incoming requests into console.
    """

    async def middleware(request):
        print(f"Incoming request: {request.method} {request.path_qs}")
        response = await handler(request)
        return response

    return middleware