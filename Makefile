RUN=PYTHONPATH=. python

examples:
	$(RUN) examples/hello.py generate a_reversed_list 1,a,2,b then dump as_json
	$(RUN) examples/fire-group.py ingestion run
	$(RUN) examples/fire-group.py digestion run
	$(RUN) examples/fire-group.py digestion status
	$(RUN) examples/fire-group.py ingestion run then digestion run status
	$(RUN) examples/fire-group.py --all ingestion run then digestion run status
	$(RUN) examples/fire-group.py --all ingestion run then digestion volume 2 run status
	$(RUN) examples/globals.py left write then right readwrite then left read
	$(RUN) examples/nested.py commands run then submenu commands run then commands run then submenu subsubmenu commands run
	$(RUN) examples/version.py --all hello then version

tag:
	git tag ${TAG} -m "${MSG}"
	git push --tags

requirements: .python-version requirements.txt
	@pip install --upgrade -r requirements.txt > /dev/null

upgrade: requirements
	@pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

test: requirements
	tox
	coverage report -m

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

.PHONY: dist docs examples
