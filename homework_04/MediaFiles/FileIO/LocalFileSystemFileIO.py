from MediaFiles.FileIO.AbstractFileIO import AbstractFileIO

class LocalFileSystemFileIO(AbstractFileIO):

    def read(self):
        return self.__read_from_filesystem()

    def write(self, binary_data):
        return self.__write_to_filesystem(binary_data)

    def __read_from_filesystem(self):
        pass

    def __write_to_filesystem(self, binary_data):
        pass

    def detect_file_info(self):
        pass

    def detect_media(self):
        pass

    def __init__(self, path):
        super().__init__()
        self.path = path