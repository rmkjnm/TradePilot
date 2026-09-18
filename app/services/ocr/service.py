from paddleocr import PaddleOCR


class OCRService:

    def __init__(self):

        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang="en"
        )

    def extract(self, image_path):

        result = self.ocr.ocr(image_path)

        output = []

        for line in result[0]:

            box = line[0]
            text = line[1][0]
            confidence = float(line[1][1])

            output.append({
                "text": text,
                "confidence": confidence,
                "bbox": box
            })

        return snapshot