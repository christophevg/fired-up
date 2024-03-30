GREEN=\033[0;32m
RED=\033[0;31m
BLUE=\033[0;34m
NC=\033[0m

RUN=PYTHONPATH=. python

examples: env-run
	@echo "$(BLUE)$(RUN) examples/hello.py$(NC) $(GREEN)generate a_reversed_list 1,a,2,b then dump as_json$(NC)"
	@$(RUN) examples/hello.py generate a_reversed_list 1,a,2,b then dump as_json
	@echo "$(BLUE)$(RUN) examples/fired-up-group-minimal.py$(NC) $(GREEN)ingestion run$(NC)"
	@$(RUN) examples/fired-up-group-minimal.py ingestion run
	@echo "$(BLUE)$(RUN) examples/fired-up-group-minimal.py$(NC) $(GREEN)digestion run$(NC)"
	@$(RUN) examples/fired-up-group-minimal.py digestion run
	@echo "$(BLUE)$(RUN) examples/fired-up-group-minimal.py$(NC) $(GREEN)digestion status$(NC)"
	@$(RUN) examples/fired-up-group-minimal.py digestion status
	@echo "$(BLUE)$(RUN) examples/fired-up-group-minimal.py$(NC) $(GREEN)--all ingestion run then digestion run$(NC)"
	@$(RUN) examples/fired-up-group-minimal.py --all ingestion run then digestion run
	@echo "$(BLUE)$(RUN) examples/globals.py$(NC) $(GREEN)left write then right readwrite then left read$(NC)"
	@$(RUN) examples/globals.py left write then right readwrite then left read
	@echo "$(BLUE)$(RUN) examples/nested.py$(NC) $(GREEN)commands run then submenu commands run then commands run then submenu subsubmenu commands run$(NC)"
	@$(RUN) examples/nested.py commands run then submenu commands run then commands run then submenu subsubmenu commands run
	@echo "$(BLUE)$(RUN) examples/version.py$(NC) $(GREEN)--all hello then version$(NC)"
	@$(RUN) examples/version.py --all hello then version

.PHONY: examples
