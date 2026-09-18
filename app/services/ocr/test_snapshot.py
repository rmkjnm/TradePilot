from app.models.market_snapshot import MarketSnapshot


def test_snapshot():

    snapshot = MarketSnapshot(

        index_name="NIFTY",

        spot_price=25230,

        expiry="30 JUL",

        timestamp="2026-07-30"

    )

    assert snapshot.index_name == "NIFTY"

    assert snapshot.spot_price == 25230