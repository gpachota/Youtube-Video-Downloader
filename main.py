from tkinter import filedialog
from tkinter import *
from pytube import YouTube
import time



root = Tk()
root.geometry('600x300')
root.resizable(0,0)
root.title("Youtube video downloader")

Label(root, text = 'Youtube Video Downloader', font = 'Helvetica 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:\n', font = 'Helvetica 15 bold').pack()
link_enter = Entry(root, width = 45, textvariable = link)
link_enter.pack()

def browse_button():

	global folder_path
	global filename
	filename =  filedialog.askdirectory()
	folder_path.set(filename)
	print(filename)


def Downloader():

	if len(link.get()) != 0:

		url = YouTube(str(link.get()))
		video = url.streams.first()

		video.download(str(filename))

		downloadedlabel = Label(root, text = "DOWNLOADED", font = 'Helvetica 15')
		downloadedlabel.pack()
		downloadedlabel.after(3000, lambda: downloadedlabel.destroy())

		link_enter.after(3000, lambda: link_enter.delete(0, END))

		nextlabel = Label(root, text = "You can paste another link to download", font = 'Helvetica 15')
		nextlabel.after(3000, lambda: nextlabel.pack())
		nextlabel.after(5000, lambda: nextlabel.destroy())

	else:

		notfoundlabel = Label(root, text = "Link not found", font = 'Helvetica 15')
		notfoundlabel.pack()
		notfoundlabel.after(1000, lambda: notfoundlabel.destroy())



folder_path = StringVar()
browserlabel = Label(master=root,textvariable=folder_path)
browserlabel.pack()
button2 = Button(text="Browse", command=browse_button)
button2.pack()

emptyline = Label(root, text = "", font = 'Helvetica 15')
emptyline.pack()

button = Button(root, text = 'DOWNLOAD', font = 'Helvetica 15 bold', bg = 'pale violet red', padx = 2, command = Downloader)
button.pack()
root.bind('<Return>', button.invoke)

root.mainloop()