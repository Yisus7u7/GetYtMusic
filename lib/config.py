import configparser
from xdg import BaseDirectory
from pathlib import Path

confdir = BaseDirectory.xdg_config_home
app_config = Path(f"{confdir}/getytmusic.conf")

def mk_config():
    app_config.touch(exist_ok=True)
    # Writing Data
    config = configparser.ConfigParser()
    config.read(app_config)

    try:
        config.add_section("SETTINGS")
    except configparser.DuplicateSectionError:
        pass

    config.set("SETTINGS", "theme", "light")

    with open(app_config, "w") as config_file:
        config.write(config_file)


try:
    open(app_config)
except FileNotFoundError:
    mk_config()
