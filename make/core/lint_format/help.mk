# Help for lint and format workflows.

.PHONY: help-lint-format
help-lint-format:
	@echo [Lint and Format] $(call HELP_TOTAL,LINT_FORMAT)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make lint                           $(HELP_COLUMN_SEPARATOR)    Run Ruff checks
	@echo   make lint-fix                       $(HELP_COLUMN_SEPARATOR)    Apply safe Ruff fixes
	@echo   make lint-fix-unsafe                $(HELP_COLUMN_SEPARATOR)    Apply Ruff unsafe fixes
	@echo   make format-ruff                    $(HELP_COLUMN_SEPARATOR)    Format with Ruff
	@echo   make format                         $(HELP_COLUMN_SEPARATOR)    Format with Black
	@echo   make format-check                   $(HELP_COLUMN_SEPARATOR)    Check Black formatting without writes
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
