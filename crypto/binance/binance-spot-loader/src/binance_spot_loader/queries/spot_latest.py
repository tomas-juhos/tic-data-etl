"""Latest Spot queries."""

from binance_spot_loader.queries.base import BaseQueriesLatest


class Queries(BaseQueriesLatest):
    """Latest Spot queries."""

    UPSERT = (
        "INSERT INTO binance.spot_{interval}_latest("
        "   symbol, "
        "   id, "
        "   latest_close, "
        "   active, "
        "   source "
        ") VALUES %s "
        "ON CONFLICT (symbol) DO "
        "UPDATE SET "
        "    symbol=EXCLUDED.symbol, "
        "    id=EXCLUDED.id, "
        "    latest_close=EXCLUDED.latest_close, "
        "    active=EXCLUDED.active, "
        "    source=EXCLUDED.source;"
    )

    CORRECT_TRADING_STATUS = (
        "UPDATE binance.spot_{interval}_latest SET "
        "   active=data.active "
        "FROM (VALUES %s) AS data (symbol, active) "
        "WHERE spot_{interval}_latest.symbol = data.symbol;"
    )
