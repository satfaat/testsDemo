from pytube import YouTube


data = {
    'URL':'https://www.youtube.com/watch?v=80SsC_ZNbyI',
    'output_path': '../../'
}


def down_vd(link, dir):
    video = YouTube(link)
    video_streams = video.streams
    #video_streams = video.streams.filter(file_extension='mp4').get_by_itag(22)
    print(video_streams)
    print(video_streams.title)
    video_streams.download(filename="my first YouTube download2", 
	     output_path=dir)

down_vd(data['URL'], data['output_path'])
