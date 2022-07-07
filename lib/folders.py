from gi.repository import GLib
import os

download_folder = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD)

try:
    os.mkdir(f"{download_folder}/GetYtMusic")
    dw_app_folder = f"{download_folder}/GetYtMusic"
    pass

except FileExistsError:
    dw_app_folder = f"{download_folder}/GetYtMusic"
    pass

