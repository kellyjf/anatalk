
all: ui_format.py ui_anatalk.py icons_rc.py

ui_%.py : ui_%.ui
	pyuic4 -i 0 -o $@ $<

%_rc.py : %.qrc
	pyrcc4 $< > $@

test: all
	python app_anatalk.py

clean:
	rm -f ui*.py *.pyc

