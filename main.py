from tkinter import *
from tkinter import filedialog
import tkinter.ttk
from pytube import YouTube
import os

# functions
def setStatus(statusvar):
    status.set(statusvar)
    statusLabel.update()

def getVideo(url):
    try:
        setStatus("Connecting...")
        yt = YouTube(url)
    except Exception as e:
        setStatus("Connection Failed")
        print(e)
    else:
        setStatus("Connected")
        setDetails(yt)

def progressbar(value):
    progressvar.set(value)
    progress.update()
    progress.update_idletasks()

def downloadVideo(yt):
    progress.grid(row=0,column=0)
    video = yt.streams.filter(progressive = True, file_extension = "mp4").first()
    yt.register_on_progress_callback(downloadProgress)
    yt.register_on_complete_callback(downloadComplete)
    video.download(download_path)

def downloadProgress(stream, chunk, bytes_remaining):
    size = stream.filesize
    per = round((1-bytes_remaining/size)*100, 2)
    setStatus("Downloading"+" "+str(round((size-bytes_remaining)/1000000,2))+"/"+str(round(size/1000000,2))+"MB")
    per_var.set(str(per)+"%")
    progressbar(per)

def downloadComplete(stream,file_path):
    setStatus("Download Complete")

def setDetails(yt):
    download_folder.set(download_path)
    video_title.set(yt.title)
    video = yt.streams.filter(progressive = True, file_extension = "mp4").first()
    size = format(int(video.filesize)/1000000,".2f")
    video_size.set(str(size)+"mb")
    Label(details_frame,text="Title : ").grid(row=0,column=0,padx=10,pady=5)
    Label(details_frame,textvariable=video_title,wraplength=300).grid(row=0,column=1,columnspan=2,padx=10,pady=5)
    Label(details_frame,text="Size : ").grid(row=1,column=0,padx=10,pady=10)
    Label(details_frame,textvariable=video_size).grid(row=1,column=1,padx=10,pady=5)
    Label(details_frame,text="Download Folder : ",wraplength=200).grid(row=2,column=0,padx=10,pady=5)
    Entry(details_frame,textvariable=download_folder,width=30).grid(row=2,column=1,padx=10,pady=5,ipady=3)
    Button(details_frame,text="Browse",command=browse_folder).grid(row=2,column=2)
    download_button = Button(details_frame,text="Download",bg="green",fg="white",command=lambda:downloadVideo(yt))
    download_button.grid(row=3,column=0,columnspan=3)

def browse_folder():
    global download_path
    download_path = filedialog.askdirectory()
    download_folder.set(download_path)

if __name__ == "__main__":
    # static variables
    root = Tk()
    root.geometry("600x550")
    root.title("YouTube Downloder")
    status = StringVar()
    video_title = StringVar()
    video_size = StringVar()
    download_folder = StringVar()
    per_var = StringVar()
    progressvar = DoubleVar()
    download_path = "/home/devil/Downloads"

    # Frames
    main_frame = Frame(root)
    main_frame.pack(fill="both",pady=25,padx=50)
    status_frame = Frame(root,bg="gray")
    status_frame.pack(side="bottom",fill="x")
    details_frame = Frame(root)
    details_frame.pack(fill=BOTH,pady=15,padx=45)
    download_frame = Frame(root)
    download_frame.pack(fill=BOTH,pady=15,padx=45)

    # widgets main frame
    Label(main_frame,text="URL : ").grid(row=0,column=0)
    url = Entry(main_frame,width=50)
    url.grid(row=0,column=1,ipady=3)
    Button(main_frame,text="Get Video",command=lambda:getVideo(url.get())).grid(row=1,column=1,columnspan=2,pady=2)

    # widgets status frame
    statusLabel = Label(status_frame,textvariable=status,bg="gray")
    statusLabel.pack(side="left")
    setStatus("Ready")

    # widgets download frame
    progress = tkinter.ttk.Progressbar(download_frame,variable=progressvar,length=400,maximum=100,value=0)
    per_label = Label(download_frame,textvariable=per_var)
    per_label.grid(row=0,column=1)

    root.mainloop()