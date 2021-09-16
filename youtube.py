from pytube import YouTube
x = True
while(x):

    url = input("Enter the URL: ")

    v = YouTube(url)

    for video in v.streams.filter(mime_type="video/mp4"):
        print(video)

    Reso = input("Enter the Res: ")

    if v.streams.filter(res=Reso).first().download('E:\\'):
        print("Done")
    else:
        print("error")

    y = input("Want to download another Video?(y/n)")
    if y == "n":
        x = False

