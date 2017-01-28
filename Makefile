
all: ui_anatalk.py

ui_%.py : ui_%.ui
	pyuic4 -i 0 -o $@ $<
