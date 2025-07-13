from MediaFiles.File import File
from MediaFiles.FileIO.LocalFileSystemFileIO import LocalFileSystemFileIO
from MediaFiles.FileIO.S3RemoteFileIO import S3RemoteFileIO
from MediaFiles.Media.Video import Video, convert


# Читаем видео-файл из S3, конвертируем в другой формат и сохраняем локально
def main():
    video_from = Video("mp4", 32)
    remote_video_file = File(
        S3RemoteFileIO("http://localhost:8080/media/video/test.mp4"),
        video_from,
    )
    remote_video_file.read()

    video_to = Video("avi", 24)
    local_video_file = File(
        LocalFileSystemFileIO("test.mp4"),
        video_to,
        remote_video_file.info
    )
    local_video_file.binary_data = convert(
        remote_video_file.binary_data,
        video_from,
        video_to
    )
    local_video_file.write()

if __name__ == "__main__":
    main()