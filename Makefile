all: ui

ui: ui_customizer.py

ui_customizer.py: ui/customizer.ui
	pyside-uic $^ -o $@

deb:
	python setup.py --command-packages=stdeb.command bdist_deb
