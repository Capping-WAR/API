# pgapi
# Author: Daniel Nicolas Gisolfi

repo=pgapi
version=1.0.0

intro:
	@echo "\n$(repo) v$(version)"

init:
	@python3 -m pip install -r requirements.txt

clean:
	- rm -r ./build 
	- rm -r ./dist
	- m -r ./$(repo).egg-info

test:
	@python3 -m pytest

build:
	@python setup.py sdist

publish:
	@python3 -m twine upload dist/*

install:
	@python3 -m pip install .

uninstall:
	@python3 -m pip uninstall $(repo)==$(version)

.PHONY: init clean test build