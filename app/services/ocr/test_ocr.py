from app.services.ocr.service import OCRService

ocr = OCRService()

result = ocr.extract(
    "uploads/analysis_1/nifty_chart.png"
)

for item in result:
    print(item)