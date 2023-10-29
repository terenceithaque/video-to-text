# Programme pour convertir l'audio d'une vidéo en un fichier texte
from tkinter import *
from tkinter import filedialog
import moviepy.editor as mp
import speech_recognition as sr
from os.path import basename
import vlc


class Application(Tk):
    "Application"

    def __init__(self):
        "Constructeur de l'application"
        super().__init__()  # Initialiser le constructeurs
        # Ajouter une barre de menu à l'application
        self.barre_menu = Menu(self, tearoff=0)
        # Ajouter un menu "Fichier"
        self.menu_fichier = Menu(self.barre_menu, tearoff=0)
        self.menu_fichier.add_command(
            label="Ouvrir un fichier vidéo...", command=self.open_video)

        self.menu_fichier.add_command(
            label="Convertir l'audio en texte", command=None)

        self.barre_menu.add_cascade(label="Fichier", menu=self.menu_fichier)

        self.video_frame = Frame(self, width=1000, height=1000)
        self.video_frame.pack()

        self.frame_winfo_id = self.video_frame.winfo_id()

        self.config(menu=self.barre_menu)

    def open_video(self):
        "Ouvrir un fichier vidéo"
        video_path = filedialog.askopenfilename(title="Ouvrir un fichier vidéo", filetypes=[
                                                ("Fichier MP4", "*.mp4"), ("Fichier AVI", "*.avi")])

        instance = vlc.Instance()
        player = instance.media_player_new()

        player.set_hwnd(self.frame_winfo_id)

        media = instance.media_new(video_path)
        player.set_media(media)
        player.play()

        self.title(basename(video_path))


app = Application()
app.mainloop()
