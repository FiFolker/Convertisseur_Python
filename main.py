from pytube import *



url = input("Met le lien de ta vidéo/playlist ici : \n>>")
#yt = YouTube(url)


#yt.streams.get_audio_only().download(filename=mp3, max_retries=5)


p = Playlist(url)


for videos in p.videos:
	mp4 = f"{videos.title}.mp4"
	print("Téléchargement : ", videos.title)
	videos.streams.first().download(filename=mp4, max_retries=5)