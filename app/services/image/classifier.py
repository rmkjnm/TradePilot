class ImageClassifier:

    @staticmethod
    def classify(image_type):

        mapping = {

            "nifty_chart": "chart",

            "option_chart": "chart",

            "option_chain": "table",

            "open_interest": "table",

            "market_depth": "depth"

        }

        return mapping.get(
            image_type,
            "unknown"
        )