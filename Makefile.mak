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

.PHONY: examples
