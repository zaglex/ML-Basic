from abc import ABC, abstractmethod

class AbstractFileIO(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, binary_data):
        pass

    @abstractmethod
    def detect_media(self):
        pass

    @abstractmethod
    def detect_file_info(self):
        pass
