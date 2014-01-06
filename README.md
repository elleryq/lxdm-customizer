# lxdm-customizer

lxdm-customizer is a tool for customizing LXDM.

# Requirement
 * Python 3
 * PySide

# Installation
## Ubuntu/Debian
You can install python-stdeb, this package can help you to get debian package.
```
python setup.py --command-packages=stdeb.command bdist_deb
```

After command is executed, you can find the debian package in deb_dist/

## Fedora/RedHat
setup.py already provide an option to create RPM package.
```
python setup.py bdist_rpm
```

## Other distribution
sudo python setup.py install
