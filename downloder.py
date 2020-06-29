from pytube import YouTube
link=input("Enter your video link\n")
yt=YouTube(link)
videos=yt.streams.all()
print(videos)
i=1
for video in videos:
    print(str(i)+"    "+str(video))
    i+=1
stream_num=int(input("Enter stream number:"))
download_video=videos[stream_num-1]
download_video.download("C:\\Users\\YASH MAHETA\\Downloads\\Video")
print("video is downloaded")