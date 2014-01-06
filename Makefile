all: ui

ui: ui_customizer.py

ui_customizer.py: ui/customizer.ui
	pyside-uic $^ -o $@

deb:
	rm -rf deb_dist
	python setup.py --command-packages=stdeb.command bdist_deb
