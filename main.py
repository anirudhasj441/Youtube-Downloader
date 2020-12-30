from tkinter import *
from pytube import YouTube
import sys

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("YouTube Downloader")
        self.status = StringVar()
        self.setStatus("ready")
        self.main_frame = Frame(self)
        self.main_frame.pack(fill="both",pady=25,padx=50)
        Label(self.status_frame,textvar=self.status,bg="gray").pack(side="left")
        Label(self.main_frame,text="URL : ").grid(column=0,row=0)
        self.url = Entry(self.main_frame)
        self.url.grid(row=0,column=1,ipady=3)
        Button(self.main_frame,text="Get Video",command=lambda : self.getVideo(self.url.get())).grid(row=1,column=0,columnspan=2,pady=2)
    def setStatus(self,status):
        self.status_frame = Frame(self,bg="gray")
        self.status_frame.pack(side="bottom",fill="x")
        self.status.set(status)
    def getVideo(self,url):
        try:
            self.setStatus("Connectng...")
            print("connecting.....")
            yt = YouTube(url)
            print(yt.title)
        except Exception as e:
            print(e)
            self.setStatus("Connection Failed")
        else:
            self.setStatus("Connected")
        details_frame = Frame(self,bg="black")
        details_frame.pack(side="top",fill=BOTH)
        Label(self.main_frame,text="Title : ",fg="white").grid(row=0,column=0)

if __name__ == "__main__":
    window = GUI()
    
    window.mainloop()