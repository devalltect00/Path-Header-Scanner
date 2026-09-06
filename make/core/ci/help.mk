# Help for CI-compatible local commands.

.PHONY: help-ci
help-ci:
	@echo [Continuous Integration] $(call HELP_TOTAL,CI)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make lint-ci                        $(HELP_COLUMN_SEPARATOR)    Run Ruff with system Python
	@echo   make format-check-ci                $(HELP_COLUMN_SEPARATOR)    Run Black checks with system Python
	@echo   make test-ci                        $(HELP_COLUMN_SEPARATOR)    Run pytest with system Python
	@echo   make check-ci                       $(HELP_COLUMN_SEPARATOR)    Run every CI-compatible check
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
