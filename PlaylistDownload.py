from pytube import Playlist

url = input("Enter playlist URL:")

p = Playlist(url)

# Your path folder
des = 'F:\\c'

for video in p.videos:
	video.streams.first().download(des)

print("done")
