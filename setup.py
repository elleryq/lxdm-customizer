import os
from subprocess import call
from glob import glob
from distutils.core import setup
from distutils.command.build import build
from distutils.command.install_data import install_data

# Screw the MANIFEST file, it just caches out of date data and messes
# up my builds.
mfst = os.path.join(os.path.dirname(__file__), "MANIFEST")
if os.path.exists(mfst):
    os.unlink(mfst)


class BuildData(build):
    def run(self):
        build.run(self)

        # Compile translations.
        call(['lrelease', 'lxdm-customizer.pro'])


class InstallData(install_data):
    def run(self):
        self.data_files.extend(self._findTranslations())
        install_data.run(self)

    def _findTranslations(self):
        translation_path = os.path.join('share', 'lxdm-customizer',
                                        'translations')
        return [(translation_path, glob('i18n/*.qm'))]


setup(name='lxdm-customizer',
      version='1.1',
      description='LXDM customization tool',
      author='Yan-ren Tsai',
      author_email='elleryq@gmail.com',
      url='https://github.com/elleryq/lxdm-customizer',
      scripts=['lxdm-customizer.py'],
      packages=['lxdm_customizer_lib'],
      license="GPL2",
      data_files=[
          ('share/applications', ['data/lxdm-customizer.desktop'])],
      cmdclass={
          'build': BuildData,
          'install_data': InstallData},
      install_requires=['PySide'],
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Environment :: X11 Applications',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: POSIX :: Linux',
          'Topic :: Desktop Environment',
          'Topic :: System',
      ],
      )
