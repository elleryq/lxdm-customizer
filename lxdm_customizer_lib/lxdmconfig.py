import os
try:
    from configparser import SafeConfigParser
except:
    from ConfigParser import SafeConfigParser
import tempfile
from .util import sudo


LXDM_CONF = "/etc/lxdm/default.conf"


class LXDMConfig(object):
    def __init__(self):
        try:
            self.parser = SafeConfigParser()
            self.parser.read(LXDM_CONF)
        except Exception as ex:
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
