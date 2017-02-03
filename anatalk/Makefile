
all: ui_format.py ui_anatalk.py

ui_%.py : ui_%.ui
	pyuic4 -i 0 -o $@ $<

test: all
	python app_anatalk.py

clean:
	rm -f ui*.py *.pyc

