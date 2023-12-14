#!/usr/bin/python
from pytube import YouTube, Playlist
import os

def downloadVid(url: str, outpath: str = "./", myTitle: str = "", extension: str = ".mp4"): 
	yt = YouTube(url)
	title = yt.title	
	print(title)	

	if (myTitle == ""):
		myTitle = title

	mp4_files = yt.streams.filter(file_extension="mp4")
	mp4_369p_files = mp4_files.get_highest_resolution()
	mp4_369p_files.download(outpath, myTitle + extension)

def downloadAudio(url: str, outpath: str = "./", myTitle: str = "", extension: str = ""):
	yt = YouTube(url)
	title = yt.title
	print(title)
	print(outpath)

	if (myTitle == ""):
		myTitle = title

	mp4_audio = yt.streams.filter(only_audio=True).first()
	out_file=mp4_audio.download(outpath)
	base, ext = os.path.splitext(out_file)
	if (extension != ""):
		command = f'ffmpeg -i out_file {myTitle}.mp3'
		os.system(command)
		os.remove(out_file)
	else:
		new_file = outpath + "/" +  myTitle + '.mp3'
		os.rename(out_file, new_file)

def downloadPlaylist(playlistUrl: str, outpath: str="./", downloadType: str="video", extension: str = ""):
	videoUrls = Playlist(playlistUrl).video_urls
	for x in range(len(videoUrls)):
	
		if (downloadType == "video"):
			downloadVid(videoUrls[x], outpath, "")

		elif (downloadType == "audio"):
			downloadAudio(videoUrls[x], outpath, "", "")

if __name__ == "__main__":
	url = None
	playlist = None
	downloadType = None
	downloadPath = None
	fileName = None
	extension = None
	while url == "" or url is None:
		url = input("Enter URL\n")
	while playlist == "" or playlist is None:
		playlist = input("Is this a playlist? Enter y or n\n")
	while downloadType == "" or downloadType is None:
		downloadType = input("Type video or audio\n")
	downloadPath = input("Enter download path (optional)\n")
	while fileName == "" or fileName is None:
		fileName = input("Enter file name (optional)\n")
	if (downloadType == "audio"):
		extension = input("Enter file extension (optional)\n")
	else:
		extension = ""
	if (playlist == "y" and (downloadType == "audio" or downloadType == "video")):
		downloadPlaylist(url, downloadPath, downloadType, extension)
	elif (downloadType == "video"):
		downloadVid(url, downloadPath, fileName, ".mp4")
	elif (downloadType == "audio"):
		downloadAudio(url, downloadPath, fileName, extension)	
	else:
		print("there was a problem with your input")
	print("Done!")
