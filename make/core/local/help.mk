# Help for Path Header Scanner commands executed locally.

.PHONY: help-local-init help-local-scan
help-local-init:
	@echo [Local Initialization] $(call HELP_TOTAL,LOCAL_INIT)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make l-init                         $(HELP_COLUMN_SEPARATOR)    Run initialization with custom variables
	@echo   make l-init-force                   $(HELP_COLUMN_SEPARATOR)    Overwrite existing initialization files
	@echo   make l-init-ask                     $(HELP_COLUMN_SEPARATOR)    Ask before overwriting files
	@echo   make l-init-all                     $(HELP_COLUMN_SEPARATOR)    Initialize all resources
	@echo   make l-init-config                  $(HELP_COLUMN_SEPARATOR)    Initialize configuration only
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-local-scan:
	@echo [Local Scan Workflows] $(call HELP_TOTAL,LOCAL_SCAN)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make l-scan TARGET=app              $(HELP_COLUMN_SEPARATOR)    Preview path-header changes
	@echo   make l-scan-apply TARGET=app        $(HELP_COLUMN_SEPARATOR)    Apply path-header changes
	@echo   make l-scan-debug TARGET=app        $(HELP_COLUMN_SEPARATOR)    Preview with debug logging
	@echo   make l-scan-apply-debug TARGET=app  $(HELP_COLUMN_SEPARATOR)    Apply changes with debug logging
	@echo   make l-scan-apply-all               $(HELP_COLUMN_SEPARATOR)    Apply changes to configured scan targets
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
