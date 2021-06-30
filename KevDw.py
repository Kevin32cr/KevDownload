#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pafy
import pyautogui
from pynput import keyboard as kb
import pyperclip
import time
from playsound import playsound

#Efectos de sonido
SoniodoDescargado = "./Effects/Descargado.wav"
SonidoError = "./Effects/Error.wav"

#Detecta Teclas
def pulsa(teclas):
    HotkeyMusica.press(escuchador.canonical(teclas))
    HotkeyVideo.press(escuchador.canonical(teclas))
#Detecta Teclas
def suelta(teclas):
    HotkeyMusica.release(escuchador.canonical(teclas))
    HotkeyVideo.release(escuchador.canonical(teclas))

#Obteniene el link del video para descargar 
def ObtenerLink():
    pyautogui.moveTo(180, 58)
    time.sleep(0.2)
    pyautogui.click(clicks=1)
    pyautogui.hotkey('ctrl','c')

#Comprueba si el link es de youtube
def ComprobarSiesYouTube():
    ObtenerLink()
    if str(pyperclip.paste())[:23] == 'https://www.youtube.com': 
            return "https://youtu.be/" + str(pyperclip.paste())[32:]
    else:
        return False

def DescargarMusica():
    try:
        pafy.new(ComprobarSiesYouTube()).getbestaudio().download(filepath="./Descargas/Musicas")
        print("[-] ¡Musica Descargada! [-]")
        playsound(SoniodoDescargado)
    except:
        playsound(SonidoError)
        print('[/] Error al descargar Musica [/]')

def DescargarVideo():
    try:
        pafy.new(ComprobarSiesYouTube()).getbest().download(filepath="./Descargas/Videos")
        print("[-] ¡Video Descargado! [-]")
        playsound(SoniodoDescargado)
    except:
        playsound(SonidoError)
        print('[/] Error al descargar video [/]')

ctrlM = kb.HotKey.parse('<shift>+1')
HotkeyMusica = kb.HotKey(ctrlM, DescargarMusica)

ctrlV = kb.HotKey.parse('<shift>+2')
HotkeyVideo = kb.HotKey(ctrlV, DescargarVideo)

with kb.Listener(pulsa, suelta) as escuchador:
    escuchador.join()