# Help for aggregate quality workflows.

.PHONY: help-quality-assurance
help-quality-assurance:
	@echo [Quality Assurance] $(call HELP_TOTAL,QA)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make fix                            $(HELP_COLUMN_SEPARATOR)    Apply Black and safe Ruff fixes
	@echo   make check                          $(HELP_COLUMN_SEPARATOR)    Run format, lint, and test validation
	@echo   make qa                             $(HELP_COLUMN_SEPARATOR)    Apply fixes and then validate
	@echo   make ci                             $(HELP_COLUMN_SEPARATOR)    Run the Compose-based CI workflow
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
