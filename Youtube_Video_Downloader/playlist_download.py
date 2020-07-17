from pytube import Playlist # import Playlist to download

# Create a variable and provide link of playlist
playlist = Playlist("https://www.youtube.com/playlist?list=PLzCxunOM5WFJxaj103IzbkAvGigpclBjt")

# Iterate through each video in playlist
for video in playlist:
	video.streams.get_highest_resolution().download("C:/Users/Tanu-PC/Videos")      # download the video into given path