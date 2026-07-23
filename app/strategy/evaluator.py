class StrategyEvaluator:

    def calculate_score(self, inputs):

        score = 0

        if inputs["trend"] == "Bullish":
            score += 25

        if inputs["momentum"] == "Strong":
            score += 20

        if inputs["volume"] == "High":
            score += 15

        if inputs["oi"] == "Bullish":
            score += 20

        if inputs["risk_reward"] >= 2:
            score += 10

        return score