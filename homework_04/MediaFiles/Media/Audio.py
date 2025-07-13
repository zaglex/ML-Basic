import BaseMedia

class Audio(BaseMedia):
    def __init__(self, media_format, album):
        super().__init__(media_format)
        self.album = album

