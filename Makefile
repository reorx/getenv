.PHONY: test

test:
	@nosetest -v .

publish:
	python setup.py sdist bdist_wheel upload
