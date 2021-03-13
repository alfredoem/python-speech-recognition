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