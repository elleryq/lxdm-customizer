# -*- coding: utf-8 -*-

X11_DEFAULT_DISPLAY_MANAGER = "/etc/X11/default-display-manager"


def isDisplayManagerLXDM():
    with open(X11_DEFAULT_DISPLAY_MANAGER) as f:
        content = f.readline()
        if content.find('lxdm') > 0:
            return True
    return False
