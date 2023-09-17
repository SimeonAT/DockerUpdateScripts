all: main

main:
	python3 ./scripts/main.py

test:
	python3 ./scripts/e2e.py

install:
	pip3 install docker