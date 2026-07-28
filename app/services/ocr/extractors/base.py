from abc import ABC, abstractmethod


class BaseExtractor(ABC):

    @abstractmethod
    def extract(self, image_path):
        """
        Returns structured data extracted
        from a processed image.
        """
        pass