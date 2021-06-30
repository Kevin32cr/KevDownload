#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pafy
import pyautogui
from pynput import keyboard as kb
import pyperclip
import time
from playsound import playsound

"""
 [+] Intrucciones [+]
 -> Ejecutar cualquier navegador en pantalla completa [ NO F11]
 -> Para descargar musicas precionar shift + 1
 -> Para descargar videos precionar shift + 2
 
 [+] ¿Errores? [+]
 -> Si al precionar cualquier shortcut para descargar
 video/musica se escucha un sonido de error
 modificar en la linea '40'pyautogui.moveTo(180, 58) las cordenadas
 para poder posicionar el cursor en la URL 
"""

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

#Descargar musica de youtube 
def DescargarMusica():
    try:
        pafy.new(ComprobarSiesYouTube()).getbestaudio().download(filepath="./Descargas/Musicas")
        print("[-] ¡Musica Descargada! [-]")
        playsound(SoniodoDescargado)
    except:
        playsound(SonidoError)
        print('[/] Error al descargar Musica [/]')
        
#Descargar video de youtube 
def DescargarVideo():
    try:
        pafy.new(ComprobarSiesYouTube()).getbest().download(filepath="./Descargas/Videos")
        print("[-] ¡Video Descargado! [-]")
        playsound(SoniodoDescargado)
    except:
        playsound(SonidoError)
        print('[/] Error al descargar video [/]')

#Detecta shortcut y llama a la funcion a ejecutar
ctrlM = kb.HotKey.parse('<shift>+1')
HotkeyMusica = kb.HotKey(ctrlM, DescargarMusica)

#Detecta shortcut y llama a la funcion a ejecutar
ctrlV = kb.HotKey.parse('<shift>+2')
HotkeyVideo = kb.HotKey(ctrlV, DescargarVideo)

#Listener para detectar teclas
with kb.Listener(pulsa, suelta) as escuchador:
    escuchador.join()