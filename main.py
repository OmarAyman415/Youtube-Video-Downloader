from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PL_yseowcuqYJc7wXtGIsshYp1B_W0M-ZK')

des = 'F:\\c'

for video in p.videos:
	video.streams.first().download(des)

print("done")