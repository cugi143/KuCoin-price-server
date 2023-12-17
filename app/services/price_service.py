from typing import List

from app.utils.database import Session
from app.models import Currency
import ccxt.async_support as ccxt


async def get_currency_price(currency: str) -> float:
    """
    Get the price of a currency from KuCoin. Saves the price to the database.
    :param currency: String representing the currency.
    :return: Dictionary containing the currency and price.
    """
    exchange = ccxt.kucoin()
    session = None

    try:
        # Fetch ticker data for the specified currency
        ticker = await exchange.fetch_ticker(f"{currency}/USDT")

        bid_price = ticker['bid']

        # Save data to the database
        session = Session()
        currency_entry = Currency(currency=currency, price=bid_price)
        session.add(currency_entry)
        session.commit()

        return bid_price

    except ccxt.ExchangeError as e:
        # Handle currency not found error
        raise ValueError(f"Currency '{currency}' not found on KuCoin") from e
    except Exception as e:
        raise e
    finally:
        if session:
            session.close()
        await exchange.close()


async def get_price_history(page: int) -> List[dict]:
    """
    Get the price history for all currencies from the database.
    :param page: Integer representing the page number.
    :return: List of dictionaries containing the price history.
    """
    session = Session()

    try:
        page_size = 10
        offset = (page - 1) * page_size
        history = session.query(Currency).order_by(Currency.date_.desc()).offset(offset).limit(page_size).all()
        return [{'currency': entry.currency, 'price': entry.price, 'date': entry.date_.isoformat()} for entry in
                history]

    except Exception as e:
        raise e
    finally:
        session.close()


async def delete_price_history():
    """
    Delete all currency price history from the database.
    :return:
    """
    session = Session()

    try:
        session.query(Currency).delete()
        session.commit()
    except Exception as e:
        raise e
    finally:
        session.close()
