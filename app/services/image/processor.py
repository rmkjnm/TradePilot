import cv2
import numpy as np


class ImageProcessor:

    @staticmethod
    def load(path):
        return cv2.imread(path)

    @staticmethod
    def grayscale(image):
        return cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

    @staticmethod
    def denoise(image):
        return cv2.GaussianBlur(
            image,
            (3, 3),
            0
        )

    @staticmethod
    def threshold(image):
        return cv2.adaptiveThreshold(
            image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            15,
            8
        )

    @staticmethod
    def preprocess(path):

        image = ImageProcessor.load(path)

        gray = ImageProcessor.grayscale(image)

        blur = ImageProcessor.denoise(gray)

        thresh = ImageProcessor.threshold(blur)

        return thresh