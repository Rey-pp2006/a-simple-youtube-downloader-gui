# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 02:22:31 2021

@author: rsh110520
"""

from tkinter import *
from pytube import YouTube
from tkinter import messagebox
from tkinter import filedialog
import os

root=Tk()
root.title("YouTube Downloader")
root.geometry('520x300')
root.minsize(520,300)
root.maxsize(520,300)


def Browse_path():
    download_path.delete(0,END)
    Path_download=filedialog.askdirectory()
    path.set(Path_download)
    

def Downloader():
    
    Link=str(link.get())
    Path=str(path.get())
    try:
        url=YouTube(Link)
        video=url.streams.first()
        video.download(Path)
        download_path.delete(0,END)
        video_link.delete(0,END)

        
        downloaded=messagebox.showinfo("Downloaded" , f"Your YouTube Vidoe Downloaded Successfully at {path.get()}/{url.title}")
    except:
        not_downloaded=messagebox.showerror("Problem" , "there is a problem ! download process failed !")    
    
    
    
#welcome label 
welcome_lab=Label(root , text = "Welcome to YouTube downloader",fg="#ffffff",bg="#4d0000" , font= "Aharoni 21 bold")
welcome_lab.grid(column=0, row=0 , pady= (0,40) , ipady=30 , ipadx=30, columnspan=3)


link=StringVar()
path=StringVar()


Video_link_lab=Label(root,  text = 'Paste Link Here:',font = 'Calibri 12 bold',fg="#4d0000")
Video_link_lab.grid(row=1 , column=0,pady=(0,20))

video_link=Entry(root , width =50 ,textvariable=link ,bd=3 , fg="#0000ff")
video_link.grid(row=1,column=1 , pady=(0,20) , columnspan=3)


download_path_lab=Label(root,  text = '         Download Path:            ',font = 'Calibri 12 bold',fg="#4d0000")
download_path_lab.grid(row=2 , column=0 )

download_path=Entry(root , width =50 ,textvariable=path ,bd=3 , fg="#0000ff")
download_path.grid(row=2,column=1)

browse_button=Button(root, text="Browse",command=Browse_path,font = 'Calibri 10 bold',bg="#4d0000",fg="#ffffff",bd=3)
browse_button.grid(row=2,column=1 , padx=(250,0))



Download_button=Button(root,text = 'DOWNLOAD', font = 'Calibri 15 bold',bg="#4d0000",fg="#ffffff",bd=3,  command = Downloader)
Download_button.grid(row=3,column=0 , columnspan=2 , pady=(40,0) , ipadx=200)
        




root.mainloop()
