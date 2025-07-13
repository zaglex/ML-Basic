from MediaFiles.Media.BaseMedia import BaseMedia


class Video(BaseMedia):
    def __init__(self, media_format, fps):
        super().__init__(media_format)
        self.fps = fps

def convert(binary_data, VideoFrom: Video, VideoTo: Video):
    pass

