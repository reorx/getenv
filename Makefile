.PHONY: test

test:
	@nosetest -v .

build-dist:
	python setup.py sdist bdist_wheel

publish: build-dist
	python -m twine upload --skip-existing $(shell ls -t dist/*.whl | head -1)
