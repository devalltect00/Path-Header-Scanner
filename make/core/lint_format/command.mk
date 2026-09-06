# Ruff and Black linting and formatting workflows.

LINT_FORMAT_COMMANDS_LIST := lint lint-fix lint-fix-unsafe format-ruff format format-check
$(foreach cmd,$(LINT_FORMAT_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,LINT_FORMAT,$(cmd),LOCAL)))

.PHONY: lint lint-fix lint-fix-unsafe format-ruff format format-check
lint: check-venv
	"$(PYTHON)" -m $(RUFF) check $(SOURCE_DIRS)

lint-fix: check-venv
	"$(PYTHON)" -m $(RUFF) check $(SOURCE_DIRS) --fix

lint-fix-unsafe: check-venv
	"$(PYTHON)" -m $(RUFF) check $(SOURCE_DIRS) --fix --unsafe-fixes

format-ruff: check-venv
	"$(PYTHON)" -m $(RUFF) format $(SOURCE_DIRS)

format: check-venv
	"$(PYTHON)" -m $(BLACK) $(SOURCE_DIRS)

format-check: check-venv
	"$(PYTHON)" -m $(BLACK) $(SOURCE_DIRS) --check
