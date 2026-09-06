# Help for Path Header Scanner Docker commands.

.PHONY: help-docker-build help-docker-testing help-docker-init help-docker-scan
help-docker-build:
	@echo [Docker Image Builds] $(call HELP_TOTAL,DOCKER_INFRASTRUCTURE)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make d-build-base                   $(HELP_COLUMN_SEPARATOR)    Build the base image
	@echo   make d-build-dev                    $(HELP_COLUMN_SEPARATOR)    Build the development image
	@echo   make d-build-prod                   $(HELP_COLUMN_SEPARATOR)    Build the production image
	@echo   make d-build-all                    $(HELP_COLUMN_SEPARATOR)    Build all Path Header Scanner images
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-docker-testing:
	@echo [Docker Testing] $(call HELP_TOTAL,DOCKER_TESTING)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make d-test                         $(HELP_COLUMN_SEPARATOR)    Run tests in the development image
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-docker-init:
	@echo [Docker Initialization] $(call HELP_TOTAL,DOCKER_INIT)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make d-init                         $(HELP_COLUMN_SEPARATOR)    Run initialization in the production image
	@echo   make d-init-force                   $(HELP_COLUMN_SEPARATOR)    Overwrite initialization files
	@echo   make d-init-ask                     $(HELP_COLUMN_SEPARATOR)    Ask before overwriting files
	@echo   make d-init-all                     $(HELP_COLUMN_SEPARATOR)    Initialize all resources
	@echo   make d-init-config                  $(HELP_COLUMN_SEPARATOR)    Initialize configuration only
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-docker-scan:
	@echo [Docker Scan Workflows] $(call HELP_TOTAL,DOCKER_SCAN)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make d-scan TARGET=app              $(HELP_COLUMN_SEPARATOR)    Preview path-header changes
	@echo   make d-scan-apply TARGET=app        $(HELP_COLUMN_SEPARATOR)    Apply path-header changes
	@echo   make d-scan-debug TARGET=app        $(HELP_COLUMN_SEPARATOR)    Preview with debug logging
	@echo   make d-scan-apply-debug TARGET=app  $(HELP_COLUMN_SEPARATOR)    Apply with debug logging
	@echo   make d-scan-apply-all               $(HELP_COLUMN_SEPARATOR)    Apply to configured scan targets
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
