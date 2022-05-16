from webbrowser import get
from lib import PySimpleGUI as sg
import pyperclip as clipboard
from os import system, path, popen, environ, chdir


def get_backend():
    if path.isfile("./lib/youtube-dl"):
        environ["YOUTUBE_DL"]="./lib/youtube-dl"

    elif path.isfile("/opt/com.ys.apps/getytmusic/lib/youtube-dl"):
        environ["YOUTUBE_DL"]="/opt/com.ys.apps/getytmusic/lib/youtube-dl"

    elif path.isfile("/data/data/com.termux/files/usr/opt/com.ys.apps/getytmusic/lib/youtube-dl"):
        environ["YOUTUBE_DL"]="/data/data/com.termux/files/usr/opt/com.ys.apps/getytmusic/lib/youtube-dl"

    else:
        print("ERROR: Not fount youtube-dl executable")

dl_args=" --embed-thumbnail --extract-audio --audio-quality 0 --audio-format mp3 "

#xdg_dirs = popen("cat ~/.config/user-dirs.dirs | grep -Po \'XDG_DOWNLOAD_DIR=\"\K.+(?=\")\'").read()
#system("export" + xdg_dirs)
#environ["XDG_DOWNLOAD_DIR"]=xdg_dirs
#dw_dir = environ.get("XDG_DOWNLOAD_DIR")
#print(f"Download dir = {dw_dir}")
#system(f"mkdir -p {dw_dir}/YtMusic")


paste_icon = "./img/paste.png"
dw_icon = "./img/dw.png"
clear_icon = "./img/clear.png"
bg_window = "./img/music.png"

df_font = ("Roboto 11")
sg.theme("Material2")

layout = [
    [
        sg.Text("Ingrese la url", font=df_font),

        sg.Button(image_filename=clear_icon, button_color="#FFFFFF",
        tooltip="Limpiar contenido", key="-CLEAR-"),

        sg.Button(image_filename=paste_icon, button_color="#FFFFFF", 
        tooltip="Pegar portapapeles", key="-PASTE-"),

        sg.Input(key="-INPUT-", background_color="#EEE2E2", text_color="#000000"),

        sg.Button(image_filename=dw_icon, button_color="#FFFFFF", 
        tooltip="Descargar", key="-DW-")
    ],

]

window = sg.Window("GetYtMusic", layout, resizable=False, alpha_channel=1.0)
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "-CLEAR-":
        window["-INPUT-"].update("")

    elif event == "-PASTE-":
        window["-INPUT-"].update(clipboard.paste())

    elif event == "-DW-":
        chdir(environ.get("HOME") + "/Descargas")
        get_backend()
        system(environ.get("YOUTUBE_DL") + dl_args + values["-INPUT-"])

    else:
        txt="Hubo un error inesperado, por favor\n"
        txt+="abra un problema en nuestro repositorio en github."

        sg.PopupError(txt,
            title="App Error"
                        )

