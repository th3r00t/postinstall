from src.lib.resources import Dotfiles, UserData
from src.lib.installers import ExtraPackages
from src.lib.environment import Hosts, HostEntry, UserShell
from pprint import pprint
import shutil, os, sys
from pathlib import Path

ud = UserData()
df = Dotfiles(ud)
ep = ExtraPackages(ud)
hs = Hosts(ud)

def restart():
    os.execv(sys.executable, ['python'] + sys.argv)

banner_title = f"ipython dev env".center(shutil.get_terminal_size().columns, " ")
print(banner_title)
print(f"Available structs: ud, df, ep\nAvailable commands: restart()")
print("Testing UserShell(ud)")
