# Pytest workflows for local development.

TESTING_COMMANDS_LIST := test test-verbose test-cov test-cov-html
$(foreach cmd,$(TESTING_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,TESTING,$(cmd),LOCAL)))

.PHONY: test test-verbose test-cov test-cov-html
test: check-venv
	"$(PYTHON)" -m $(PYTEST)

test-verbose: check-venv
	"$(PYTHON)" -m $(PYTEST) -v

test-cov: check-venv
	"$(PYTHON)" -m $(PYTEST) --cov=$(PROJECT_PACKAGE) --cov-report=term-missing

test-cov-html: check-venv
	"$(PYTHON)" -m $(PYTEST) --cov=$(PROJECT_PACKAGE) --cov-report=html
