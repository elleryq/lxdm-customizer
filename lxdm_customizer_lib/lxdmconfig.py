import os
import sys
from ConfigParser import SafeConfigParser
import tempfile
import re


LXDM_CONF = "/etc/lxdm/default.conf"


def sudo(cmd, msg=""):
    """
    refer from http://python.org.ar/Xdg-Sudo
    """
    from subprocess import call, check_output
    # non-root check, because if you are root, all this is pointless
    if os.geteuid() == 0:
        raise Exception(" ERROR: Do not run as root...")

    # Test which tools exist
    kdesudo = os.path.exists('/usr/bin/kdesudo')
    gtksudo = os.path.exists('/usr/bin/gksudo')

    realCmd = []

    # If we have at least one of them, check which one to use.
    if kdesudo or gtksudo:
        if kdesudo and gtksudo:
            # Test if gnome runs
            ps_result = check_output(["ps", "-ae"])
            if re.search("(gnome-session|lxsession)", ps_result):
                useGnome = True
            else:
                useGnome = False
        elif kdesudo and (not gtksudo):
            useGnome = False
        elif (not kdesudo) and gtksudo:
            useGnome = True
        # really run it
        if useGnome:
            realCmd.append("gksudo")
            if msg:
                realCmd.append("-m")
                realCmd.append(msg)
        else:
            realCmd.append("kdesudo")
            realCmd.append("-d")
            if msg:
                realCmd.append("--comment")
                realCmd.append(msg)
        realCmd.append(cmd)
        call(realCmd)
    else:
        # we dont have gksudo or kdesudo, OMFG!
        sudocmd = "xterm -e \"echo 'Neither \\\"gksudo\\\" nor \\\"kdesudo\\\" have been found on your machine. Thus, \\\"sudo\\\" is being used. Please leave this window open until the program has finished. Your are asked for your password below.'; sudo "+cmd+"; sleep 1\""
        os.system(sudocmd)


class LXDMConfig(object):
    def __init__(self):
        try:
            self.parser = SafeConfigParser()
            self.parser.read(LXDM_CONF)
        except Exception, ex:
            raise ex

    def __getattr__(self, attr):
        try:
            return object.__getattr__(self, attr)
        except AttributeError:
            return getattr(self.parser, attr)

    def save(self):
        outf = tempfile.NamedTemporaryFile('w+t', delete=False)
        self.parser.write(outf)
        outf.close()
        self.doCopy(outf.name)
        os.unlink(outf.name)

    def saveAs(self, outfile):
        outf = open(outfile, "wt")
        self.parser.write(outf)
        outf.close()

    def doCopy(self, tmpfile):
        cmd = "cp {0} {1}".format(tmpfile, LXDM_CONF)
        sudo(cmd, "Override system configuration.")
