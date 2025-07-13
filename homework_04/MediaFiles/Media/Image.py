import BaseMedia

class Image(BaseMedia):
    def __init__(self, media_format, resolution):
        super().__init__(media_format)
        self.resolution = resolution

