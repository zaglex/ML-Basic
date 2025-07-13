from MediaFiles.FileIO.AbstractFileIO import AbstractFileIO
from MediaFiles.FileInfo import FileInfo
from MediaFiles.Media.BaseMedia import BaseMedia


class File:
    def __init__(self, io: AbstractFileIO, media: BaseMedia = None, info: FileInfo = None):
        self.io = io
        if media is None:
            media = self.io.detect_media()
        if info is None:
            info = self.io.detect_file_info()
        self.media = media
        self.info = info
        self.binary_data = ""

    def write(self):
        self.io.write(self.binary_data)

    def read(self):
        self.binary_data = self.io.read()