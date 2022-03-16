import tkinter

from pytube import YouTube, Playlist
from tkinter import *

window = Tk()
window.title("Convertisseur")
cnv = Canvas(window, width=800, height=600)
cnv.pack()
window.resizable(width=False, height=False)


def playlist_dl(url):
	p = Playlist(url)
	for video in p.videos:
		mp4 = f"{video.title}.mp4"
		print("Téléchargement : ", video.title)
		video.streams.first().download(filename=mp4, max_retries=5)

text = tkinter.StringVar()

url_playlist = Entry(window, textvariable=text)
button_playlist = Button(window, text="Télécharger")

print(url_playlist.get())

#url_playlist.grid(row=0, column=0, pady=150, padx=250, ipadx=100)
#button_playlist.grid(row=1, column=0, padx=150)
url_playlist.pack()
button_playlist.pack()



button_playlist.bind('<download_playlist>', playlist_dl(text.get()))

window.mainloop()

""""
url = input("Met le lien de ta vidéo/playlist ici : \n>>")
#yt = YouTube(url)


#yt.streams.get_audio_only().download(filename=mp3, max_retries=5)
"""
