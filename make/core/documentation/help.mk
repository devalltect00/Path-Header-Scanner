# Help for MkDocs commands.

.PHONY: help-documentation
help-documentation:
	@echo [Documentation] $(call HELP_TOTAL,DOCUMENTATION)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make docs-serve                     $(HELP_COLUMN_SEPARATOR)    Serve documentation locally
	@echo   make docs-build                     $(HELP_COLUMN_SEPARATOR)    Build the documentation site
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
