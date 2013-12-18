# -*- coding: utf-8 -*-
import os
from glob import glob
import pwd


LXDM_LIB_DIR = os.path.join(os.sep, 'usr', 'lib', 'lxdm')
GTK_THEMES_DIR = os.path.join(os.sep, 'usr', 'share', 'themes')
LXDM_THEMES_DIR = os.path.join(os.sep, 'usr', 'share', 'lxdm', 'themes')


def findGreeters():
    filenames = glob(os.path.join(LXDM_LIB_DIR, 'lxdm-greeter-*'))
    greeters = [(os.path.basename(fn), fn) for fn in filenames]
    return sorted(greeters)


def findGtkThemes():
    def isGtkThemeExisted(p):
        if os.path.exists(os.path.join(p, 'gtk-2.0')):
            return True
        return False
    filenames = glob(os.path.join(GTK_THEMES_DIR, '*'))
    themes = [(os.path.basename(fn), fn) for fn in filenames if
              isGtkThemeExisted(fn)]
    return sorted(themes)


def findLXDMThemes():
    filenames = glob(os.path.join(LXDM_THEMES_DIR, '*'))
    themes = [(os.path.basename(fn), fn) for fn in filenames]
    return themes


def getSystemUsers():
    users = pwd.getpwall()
    return [user.pw_name for user in users if
            user.pw_uid >= 1000 and user.pw_uid < 65534 and
            not user.pw_shell == '/sbin/nologin']
