#use youtube-dl package: commonand-line program to download videos from Youtube.com and other vedio sites

from webbrowser import get
import youtube_dl

ydl = youtube_dl.YoutubeDL()


def get_vedio_infos(url):
    with ydl:
        result = ydl.extract_info(
            url,
            download = False
        )
    if "entries" in result:
        return result["entries"][0]
    return result


def get_audio_url(vedio_info):
    for f in vedio_info["format"]:
        if f["ext"] == "m4a":
            return f["url"]



if __name__ == "__main__":
    video_info = get_vedio_infos("link")
    audio_url = get_audio_url(video_info)
    print(audio_url)
