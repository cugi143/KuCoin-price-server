from aiohttp import web
import app.services.price_service as price_service

async def get_price(request):
    """
    GET price/{currency}
    Get price of a currency from KuCoin endpoint.
    :param request:
    :return: json response
    """

    currency = request.match_info['currency']
    try:
        price = await price_service.get_currency_price(currency)
        return web.json_response({'currency': currency, 'price': price})
    except ValueError as e:
        return web.json_response({'error': str(e)}, status=400)
    except Exception as e:
        return web.json_response({'error': f"Internal Server Error: {str(e)}"}, status=500)

async def get_price_history(request):
    """
    GET price/history
    Get price history from database endpoint.
    :param request:
    :return: json response
    """
    page = int(request.query.get('page', 1))
    try:
        history = await price_service.get_price_history(page)
        return web.json_response(history)
    except Exception as e:
        return web.json_response({'error': f"Internal Server Error: {str(e)}"}, status=500)

async def delete_price_history(request):
    """
    DELETE price/history
    Delete price history from database endpoint.
    :param request:
    :return: json response
    """
    try:
        await price_service.delete_price_history()
        return web.Response(status=204)
    except Exception as e:
        return web.json_response({'error': f"Internal Server Error: {str(e)}"}, status=500)