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

        self.barre_menu.add_cascade(label="Fichier", menu=self.menu_fichier)

        self.menu_edition = Menu(self, tearoff=0)  # Créer un menu "Edition"
        self.menu_edition.add_command(
            label="Convertir l'audio au format texte...", command=self.audio_to_text)
        self.barre_menu.add_cascade(label="Edition", menu=self.menu_edition)

        # Ajouter un menu "Lecture"
        self.menu_lecture = Menu(self.barre_menu, tearoff=0)
        self.menu_lecture.add_command(
            label="Pause  Espace", command=self.pause)
        self.menu_lecture.add_command(
            label="Reprendre la lecture     Espace", command=self.play)

        self.barre_menu.add_cascade(label="Lecture", menu=self.menu_lecture)

        self.video_frame = Frame(self, width=1000, height=1000)
        self.video_frame.pack()

        self.frame_winfo_id = self.video_frame.winfo_id()

        self.config(menu=self.barre_menu)

        self.player = None

        self.media_pause = False  # Le lecteur est-il en pause ?

        self.bind("<space>", self.play_or_pause)

    def open_video(self):
        "Ouvrir un fichier vidéo"
        global video_path
        video_path = filedialog.askopenfilename(title="Ouvrir un fichier vidéo", filetypes=[
                                                ("Fichier MP4", "*.mp4"), ("Fichier AVI", "*.avi"), ("Fichier MKV", "*.mkv"), ("Tout les formats", "*.*")])

        instance = vlc.Instance()
        self.player = instance.media_player_new()

        self.player.set_hwnd(self.frame_winfo_id)

        media = instance.media_new(video_path)
        self.player.set_media(media)
        self.player.play()

        self.title(basename(video_path))

    def video_to_audio(self):
        "Convertir la vidéo en audio"

        clip = mp.VideoFileClip(f"{video_path}")

        return clip.audio.write_audiofile(f"output.mp3")

    def pause(self):
        "Mettre le lecteur sur pause"
        self.player.set_pause(1)
        self.media_pause = True

    def play(self):
        "Reprendre la lecture"
        self.player.set_pause(0)
        self.media_pause = False

    def play_or_pause(self, event):
        "Reprendre la lecture ou mettre en pause"
        if self.media_pause == True:  # Si la pause est active
            self.play()  # Reprendre la lecture

        else:
            self.pause()  # Mettre le média en pause

    def audio_to_text(self):
        "Convertir l'audio en texte"


app = Application()
app.mainloop()
