# CI-compatible checks that use the environment's Python executable.

CI_COMMANDS_LIST := lint-ci format-check-ci test-ci check-ci
$(foreach cmd,$(CI_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,CI,$(cmd),LOCAL)))

.PHONY: lint-ci format-check-ci test-ci check-ci
lint-ci:
	"$(PYTHON_SYSTEM)" -m $(RUFF) check $(SOURCE_DIRS)

format-check-ci:
	"$(PYTHON_SYSTEM)" -m $(BLACK) --check $(SOURCE_DIRS)

test-ci:
	"$(PYTHON_SYSTEM)" -m $(PYTEST) -v

check-ci:
	@$(MAKE) --no-print-directory format-check-ci
	@$(MAKE) --no-print-directory lint-ci
	@$(MAKE) --no-print-directory test-ci
