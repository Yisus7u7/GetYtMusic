#!/bin/python3

from lib import PySimpleGUI as sg
import pyperclip as clipboard
from lib import theme, icon
from os import system, path, popen, environ, chdir

dl_args=" --embed-thumbnail --extract-audio --audio-quality 0 --audio-format mp3 "

# Nota
#xdg_dirs = popen("cat ~/.config/user-dirs.dirs | grep -Po \'XDG_DOWNLOAD_DIR=\"\K.+(?=\")\'").read()
#system("export" + xdg_dirs)
#environ["XDG_DOWNLOAD_DIR"]=xdg_dirs
#dw_dir = environ.get("XDG_DOWNLOAD_DIR")
#print(f"Download dir = {dw_dir}")
#system(f"mkdir -p {dw_dir}/YtMusic")


sg.theme_add_new('DlYtMusicDark', theme.MaterialDarkNoBorder)

df_font = ("Sans 11")
sg.theme("DlYtMusicDark")

title = "DlYtMusic"

layout = [
    [
        sg.Text("Ingrese la url:", font=df_font),

        sg.Button(image_filename=icon.clear_icon, tooltip="Limpiar contenido", key='-CLEAR-'),

        sg.Button(image_filename=icon.paste_icon, tooltip="Pegar portapapeles", key='-PASTE-'),

        sg.Input(key="-INPUT-"),

        sg.Button(image_filename=icon.dw_icon, tooltip="Descargar", key="-DW-")
    ],     

]

window = sg.Window("GetYtMusic", layout, resizable=False, alpha_channel=1.0, no_titlebar=False)
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == '-CLEAR-':
        window['-INPUT-'].update("")

    elif event == "-PASTE-":
        window['-INPUT-'].update(clipboard.paste())

    elif event == '-DW-':
        chdir(environ.get("HOME") + "/Descargas")
        system(environ.get("YOUTUBE_DL") + dl_args + values["-INPUT-"])

    else:
        txt="Hubo un error inesperado, por favor\n"
        txt+="abra un problema en nuestro repositorio en github."

        sg.PopupError(txt,
            title="App Error"
                        )

