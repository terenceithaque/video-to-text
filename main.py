# Programme pour convertir l'audio d'une vidéo en un fichier texte
from tkinter import *
import moviepy.editor as mp
import speech_recognition as sr


class Application(Tk):
    "Application"

    def __init__(self):
        "Constructeur de l'application"
        super().__init__()
