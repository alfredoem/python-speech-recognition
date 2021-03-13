SHELL := /bin/bash

init:
	python3 -m venv env

install:
	pip3 install -r requirements.txt

run:
	source env/bin/activate
	python3 ./scripts/command.py

read:
	python3 ./scripts/read.py

build:
	docker build -t python-speech-recognition-app .

start:
	docker run -it --rm \
			 --device /dev/snd \
			 -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
			 -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
			 -v ~/.config/pulse/cookie:/root/.config/pulse/cookie \
			 -v /media/dyan/project/projects/voice/:/data/voice \
			--name python-speech-recognition python-speech-recognition-app