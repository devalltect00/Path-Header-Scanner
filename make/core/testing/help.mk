# Help for local test workflows.

.PHONY: help-testing
help-testing:
	@echo [Testing] $(call HELP_TOTAL,TESTING)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make test                           $(HELP_COLUMN_SEPARATOR)    Run the test suite
	@echo   make test-verbose                   $(HELP_COLUMN_SEPARATOR)    Run tests with verbose output
	@echo   make test-cov                       $(HELP_COLUMN_SEPARATOR)    Run tests with terminal coverage
	@echo   make test-cov-html                  $(HELP_COLUMN_SEPARATOR)    Generate an HTML coverage report
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
