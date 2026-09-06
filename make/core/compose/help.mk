# Help for Path Header Scanner Docker Compose commands.

.PHONY: help-compose-infrastructure help-compose-init help-compose-scan help-compose-utilities
help-compose-infrastructure:
	@echo [Compose Infrastructure] $(call HELP_TOTAL,COMPOSE_INFRASTRUCTURE)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make c-build-base                   $(HELP_COLUMN_SEPARATOR)    Build the base Compose image
	@echo   make c-build-dev                    $(HELP_COLUMN_SEPARATOR)    Build the development app image
	@echo   make c-build-prod                   $(HELP_COLUMN_SEPARATOR)    Build the production app image
	@echo   make c-build-all                    $(HELP_COLUMN_SEPARATOR)    Build all Compose images
	@echo   make c-up                           $(HELP_COLUMN_SEPARATOR)    Start the development stack
	@echo   make c-up-build                     $(HELP_COLUMN_SEPARATOR)    Start and rebuild the development stack
	@echo   make c-up-detached                  $(HELP_COLUMN_SEPARATOR)    Start the development stack in background
	@echo   make c-down                         $(HELP_COLUMN_SEPARATOR)    Stop the development stack
	@echo   make c-down-clean                   $(HELP_COLUMN_SEPARATOR)    Stop and remove volumes and orphans
	@echo   make c-logs                         $(HELP_COLUMN_SEPARATOR)    Follow development stack logs
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-compose-init:
	@echo [Compose Initialization] $(call HELP_TOTAL,COMPOSE_INIT)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make c-init                         $(HELP_COLUMN_SEPARATOR)    Run initialization through Compose
	@echo   make c-init-force                   $(HELP_COLUMN_SEPARATOR)    Overwrite initialization files
	@echo   make c-init-ask                     $(HELP_COLUMN_SEPARATOR)    Ask before overwriting files
	@echo   make c-init-all                     $(HELP_COLUMN_SEPARATOR)    Initialize all resources
	@echo   make c-init-config                  $(HELP_COLUMN_SEPARATOR)    Initialize configuration only
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-compose-scan:
	@echo [Compose Scan Workflows] $(call HELP_TOTAL,COMPOSE_SCAN)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make c-scan TARGET=app              $(HELP_COLUMN_SEPARATOR)    Preview path-header changes
	@echo   make c-scan-apply TARGET=app        $(HELP_COLUMN_SEPARATOR)    Apply path-header changes
	@echo   make c-scan-debug TARGET=app        $(HELP_COLUMN_SEPARATOR)    Preview with debug logging
	@echo   make c-scan-apply-debug TARGET=app  $(HELP_COLUMN_SEPARATOR)    Apply with debug logging
	@echo   make c-scan-apply-all               $(HELP_COLUMN_SEPARATOR)    Apply to configured scan targets
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-compose-utilities:
	@echo [Compose Developer Utilities] $(call HELP_TOTAL,COMPOSE_UTILITIES)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make c-test                         $(HELP_COLUMN_SEPARATOR)    Run tests
	@echo   make c-lint                         $(HELP_COLUMN_SEPARATOR)    Run Ruff checks
	@echo   make c-lint-fix                     $(HELP_COLUMN_SEPARATOR)    Apply Ruff fixes
	@echo   make c-format                       $(HELP_COLUMN_SEPARATOR)    Format with Black
	@echo   make c-format-check                 $(HELP_COLUMN_SEPARATOR)    Check Black formatting
	@echo   make c-docs                         $(HELP_COLUMN_SEPARATOR)    Start the documentation service
	@echo   make c-shell                        $(HELP_COLUMN_SEPARATOR)    Open a development shell
	@echo   make c-build-package                $(HELP_COLUMN_SEPARATOR)    Build package artifacts
	@echo   make c-exec-shell                   $(HELP_COLUMN_SEPARATOR)    Open a shell in a running app container
	@echo   make c-fix                          $(HELP_COLUMN_SEPARATOR)    Apply format and lint fixes
	@echo   make c-check                        $(HELP_COLUMN_SEPARATOR)    Run format, lint, and tests
	@echo   make c-qa                           $(HELP_COLUMN_SEPARATOR)    Run fix and check
	@echo   make c-ci                           $(HELP_COLUMN_SEPARATOR)    Run Compose CI validation
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
