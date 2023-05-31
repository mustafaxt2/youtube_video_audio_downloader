from pytube import YouTube
from customtkinter import *
from tkinter.messagebox import showinfo,showerror
from PIL import Image,ImageTk
import urllib.request

class YoutubeGUI:
    def __init__(self):
        self.root = CTk()
        self.root.title("Youtube Video Downloader")
        self.root.geometry("400x100")
        self.root.resizable(width=False, height=False)
        self.root.iconbitmap("youtube.ico")
        self.root.configure(bg="black")

        self.label=CTkLabel(master=self.root,
            width=75,
            height=10,
            corner_radius=8,
            bg_color="transparent",
            text="Note that some videos cannot be downloaded due to:\n-Copyrights\n-Age Restrictions etc.",
            text_color="red").pack(pady=5)
        
        self.ent1=CTkEntry(master=self.root,
                            placeholder_text="Paste the link of the video".center(55),
                            placeholder_text_color="orange",
                            width=250,
                            height=10,
                            corner_radius=8,
                            border_width=2,
                            border_color="grey",
                            bg_color="transparent",)
        self.ent1.pack(pady=5)

        def enter(event):
            result=self.ent1.get()
            if len(result) == 0:
                 showerror("Error!","Please enter a link")
            else:
                try:
                    return newWindow(result)
                
                except:
                    showerror("Error!","Please enter a appropriate link")
                    

        self.root.bind("<Return>",enter)

class newWindow:
    def __init__(self,url):
        self.url=url
        self.video=YouTube(self.url)
        self.HighResVid=self.video.streams.get_highest_resolution()
        self.audio=self.video.streams.filter(only_audio=True).first()
        self.root = CTkToplevel()
        self.root.title(self.video.title)
        self.root.geometry("400x280")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg="black")
        urllib.request.urlretrieve(self.video.thumbnail_url,
        "thumbnail.png")
        self.image=ImageTk.PhotoImage(Image.open("thumbnail.png").resize((300,200),Image.Resampling.LANCZOS))
        self.canvas=CTkCanvas(self.root,width=self.image.width(), height=self.image.height())
        self.canvas.pack()
        self.canvas.image=self.image
        self.canvas.create_image(0,0,anchor=NW,image=self.image)
        self.downloadPath=StringVar()
        optionmenu_var = StringVar(value=self.HighResVid.resolution)  # set initial value

        def optionmenu_callback(choice):
            self.HighResVid=self.video.streams.filter(resolution=choice).first()
            self.label.configure(text=f"Video Size: {round(int(self.HighResVid.filesize)*0.000001, 2)} MB\n"
                            f"Audio Size: {round(int(self.audio.filesize)*0.000001, 2)} MB\n")

        combobox = CTkOptionMenu(master=self.canvas,
                                            values=[self.HighResVid.resolution],
                                            command=optionmenu_callback,
                                            variable=optionmenu_var,
                                            corner_radius=1,
                                            bg_color="transparent",
                                            dropdown_text_color="yellow",
                                            text_color="yellow",
                                            width=5
                                            )
        combobox.place(relx=0.75,rely=0.85)
        
        try:
            vids=[self.video.streams.get_by_resolution("1080p"),self.video.streams.get_by_resolution("720p"),self.video.streams.get_by_resolution("480p"),self.video.streams.get_by_resolution("360p"),self.video.streams.get_by_resolution("144p")]
            vidsRes=[]

            for x in vids:
                if x == None:
                    vids.remove(x)
                    
            for x in vids:
                vidsRes.append(x.resolution)

            combobox.configure(values=vidsRes)
        except:
             self.HighResVid=self.video.streams.get_highest_resolution()

        self.label=CTkLabel(master=self.root,
                        width=75,
                        height=10,
                        corner_radius=8,
                        bg_color="transparent",
                        text=f"Video Size: {round(int(self.HighResVid.filesize)*0.000001, 2)} MB\n"
                            f"Audio Size: {round(int(self.audio.filesize)*0.000001, 2)} MB\n")
        self.label.pack()

        self.ent1=CTkEntry(master=self.root,
                    textvariable=self.downloadPath,
                    width=200,
                    height=10,
                    corner_radius=8,
                    border_width=2,
                    border_color="grey",
                    bg_color="transparent",)
        self.ent1.pack()

        self.label2=CTkLabel(master=self.root,
                width=50,
                height=10,
                corner_radius=8,
                bg_color="transparent",
                fg_color="black",
                text="Download to:")
        self.label2.place(relx=0.03,rely=0.755)

        def browse():
             downloadDirectory=filedialog.askdirectory(initialdir="Your directory path",title="Save File")
             self.downloadPath.set(downloadDirectory)

        self.button0=CTkButton(master=self.root,
                width=20,
                height=20,
                corner_radius=8,
                border_width=2,
                bg_color="transparent",
                text="Browse",
                text_color="black",
                hover_color="yellow",command=browse)
        self.button0.place(relx=0.76,rely=0.745)
        

        self.button1=CTkButton(master=self.root,
                        width=20,
                        height=20,
                        corner_radius=8,
                        border_width=2,
                        bg_color="transparent",
                        text="Download Video",
                        text_color="black",
                        hover_color="yellow",command=self.download_video)
        self.button1.pack(pady=2.25)
        
        self.button2=CTkButton(master=self.root,
                        width=20,
                        height=20,
                        corner_radius=8,
                        border_width=2,
                        bg_color="transparent",
                        text="Download Audio",
                        text_color="black",
                        hover_color="yellow",command=self.download_audio)
        self.button2.pack()
        you.root.withdraw()
        def close_window():
             self.root.destroy()
             you.root.iconify()

        self.root.protocol("WM_DELETE_WINDOW",close_window)


    def download_video(self):
            downloadFolder=self.ent1.get()
            if len(downloadFolder)==0:
                    showerror("Error!","Please set the download location")
            else:
                try:
                    self.HighResVid.download(downloadFolder)
                    showinfo(title="Completed!",message="The video has been downloaded")
                except:
                    showerror(title="Error!",message="Cannot be downloaded")

    def download_audio(self):
            downloadFolder=self.ent1.get()
            if len(downloadFolder)==0:
                    showerror("Error!","Please set the download location")
            else:
                try:
                    self.audio.download(downloadFolder)
                    showinfo(title="Completed!",message="The audio has been downloaded")
                except:
                    showerror(title="Error!",message="Cannot be downloaded")
    
you=YoutubeGUI()
you.root.mainloop()