#!/usr/bin/env python
from lib.resources import UserData, Dotfiles
from lib.installers import pacman, ExtraPackages
from lib.environment import Hosts, UserShell

if __name__ == "__main__":
    ud = UserData()
    system_packages_installed = pacman(ud)
    if system_packages_installed:
        ExtraPackages(ud).install()
        Hosts(ud).sudo_write_hosts()
        Dotfiles(ud).dispatch()
        UserShell(ud)
