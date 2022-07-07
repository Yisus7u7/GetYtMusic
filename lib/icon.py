from xdg import BaseDirectory
import configparser

confdir = BaseDirectory.xdg_config_home
app_config_file = (f"{confdir}/getytmusic.conf")

app_config = configparser.ConfigParser()
app_config.read(app_config_file)

# Apply settings
icon_type = app_config.get("SETTINGS", "theme")
print(icon_type)
if icon_type == "light":
    clear_icon = "./lib/img/light/clear.png"
    paste_icon = "./lib/img/light/paste.png"
    dw_icon = "./lib/img/light/dw.png"
    pass

elif icon_type == "dark":
    clear_icon = "./lib/img/dark/clear.png"
    paste_icon = "./lib/img/dark/paste.png"
    dw_icon = "./lib/img/dark/dw.png"
    pass

else:
    print("getytmusic.conf: invalid config file")
    exit(1)
