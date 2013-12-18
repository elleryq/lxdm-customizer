all: ui

ui: ui_customizer.py

ui_customizer.py: customizer.ui
	pyside-uic $^ -o $@
