import cv2

from app.services.image.processor import ImageProcessor

image = ImageProcessor.preprocess(
    "uploads/analysis_1/nifty_chart.png"
)

cv2.imshow("Processed", image)

cv2.waitKey(0)