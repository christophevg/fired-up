tag:
	git tag ${TAG} -m "${MSG}"
	git push --tags

requirements: .python-version requirements.txt
	@pip install --upgrade -r requirements.txt > /dev/null

upgrade: requirements
	@pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

test: requirements
	tox

dist: requirements
	rm -rf $@
	python setup.py sdist bdist_wheel

publish-test: dist
	twine upload --repository testpypi dist/*

publish: dist
	twine upload dist/*

PROJECT:=`find . -name '__init__.py' -maxdepth 2 | xargs dirname | grep -v docs`

lint:
	@PYTHONPATH=. pylint --disable=W0311 ${PROJECT} | tee lint.txt

clean:
	find . -type f -name "*.backup" | xargs rm

.PHONY: dist docs
