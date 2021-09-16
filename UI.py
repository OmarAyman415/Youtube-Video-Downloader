from pytube import YouTube
x = True
while(x):

    url = input("Enter the URL: ")

    v = YouTube(url)

    for video in v.streams.filter(mime_type="video/mp4"):
        print(v.streams.get_by_resolution("720p"))

    # Reso = input("Enter the Res: ")
    #
    # if v.streams.filter(res=Reso).first().download('E:\Study\PHP\Video'):
    #     print("Done")
    # else:
    #     print("error")
    #
    # y = input("Want to donwload another Video?(y/n)")
    # if y == "n":
    #     x = False

