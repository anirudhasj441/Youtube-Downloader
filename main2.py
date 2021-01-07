from tkinter import *
import tkinter.ttk
from pytube import YouTube

# functions
def setStatus(statusvar):
    status.set(statusvar)
    statusLabel.update()

def getVideo(url):
    try:
        status_progress.pack(side="left",padx=20)
        status_progress.update()
        status_progress.start(10)
        setStatus("Connecting...")
        yt = YouTube(url)
        # status_progress.stop()
        print(yt.title)
    except Exception as e:
        setStatus("Connection Failed")
        print(e)
    else:
        setStatus("Connected")
        status_progress.stop()
        # status_progress.pack_forget()
# static variables
root = Tk()
root.geometry("300x300")
root.title("YouTube Downloder")
status = StringVar()

# Frames
main_frame = Frame(root)
main_frame.pack(fill="both",pady=25,padx=50)
status_frame = Frame(root,bg="gray")
status_frame.pack(side="bottom",fill="x")

# widgets main frame
Label(main_frame,text="URL : ").grid(row=0,column=0)
url = Entry(main_frame)
url.grid(row=0,column=1,ipady=3)
Button(main_frame,text="Get Video",command=lambda:getVideo(url.get())).grid(row=1,column=0,columnspan=2,pady=2)

# widgets status frame
statusLabel = Label(status_frame,textvariable=status,bg="gray")
statusLabel.pack(side="left")
status_progress = tkinter.ttk.Progressbar(status_frame,length=100,mode="indeterminate")
setStatus("Ready")





root.mainloop()