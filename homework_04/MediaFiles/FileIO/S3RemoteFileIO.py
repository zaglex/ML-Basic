from MediaFiles.FileIO.AbstractFileIO import AbstractFileIO

class S3RemoteFileIO(AbstractFileIO):
    def __init__(self, url):
        super().__init__()
        self.path = url

    def read(self):
        return self.__download()

    def write(self,binary_data):
        return self.__upload(binary_data)

    def detect_file_info(self):
        pass

    def detect_media(self):
        pass

    def __download(self):
        pass

    def __upload(self, binary_data):
        pass
