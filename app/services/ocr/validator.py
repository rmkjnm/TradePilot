from app.models.market_snapshot import MarketSnapshot


class SnapshotValidator:

    @staticmethod
    def validate(snapshot: MarketSnapshot):

        errors = []

        if snapshot.spot_price <= 0:
            errors.append("Invalid spot price.")

        if snapshot.atm_strike is None:
            errors.append("ATM strike missing.")

        if len(snapshot.strikes) == 0:
            errors.append("No strike data extracted.")

        return errors