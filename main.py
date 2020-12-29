from tkinter import Tk,filedialog,Frame
from pytube import YouTube

root = Tk()
frame = Frame()
entry = filedialog.askdirectory()
frame.pack()
print(entry)



root.mainloop()