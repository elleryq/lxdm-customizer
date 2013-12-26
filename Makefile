all: ui

ui: ui_customizer.py

ui_customizer.py: ui/customizer.ui
	pyside-uic $^ -o $@
