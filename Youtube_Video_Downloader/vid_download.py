from pytube import YouTube      # import YouTube

try:
    # Create a variable to pass the link of video and download the highest quality video available
    yt = YouTube("https://www.youtube.com/watch?v=qd_2lX_bwPY").streams.first()

    # save the video to specific folder
    yt.download("C:/Users/Tanu-PC/Python_Project/Youtube_Video_Downloader/Download")

except Exception as e:
    print(e)
    print("Error found")

else:
    print("Done Downloading")