# Practical examples for Path Header Scanner Make workflows.

.PHONY: help-examples
help-examples:
	@echo [Examples]
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo [Local Path Header Scanner Workflow]
	@echo   make setup
	@echo   make l-scan TARGET=app
	@echo   make l-scan-apply TARGET=app
	@$(ECHO_BLANK)
	@echo [Docker and Compose Workflow]
	@echo   make d-build-all
	@echo   make c-check
	@$(ECHO_BLANK)
	@echo [Published Image Registry Workflow]
	@echo   make r-phs-pull REMOTE_TAG=latest
	@echo   make r-doc-gen-pull REMOTE_TAG=latest
	@echo   make r-custy-pull REMOTE_TAG=latest
	@echo   make r-reflow-pull REMOTE_TAG=latest
	@$(ECHO_BLANK)
	@echo [Published Utility Runtime Workflow]
	@echo   make r-phs-scan TARGET=app REMOTE_WORKSPACE="D:/project/target"
	@echo   make r-doc-generate-smart REMOTE_WORKSPACE="D:/project/target"
	@echo   make r-custy-run-validate REMOTE_WORKSPACE="D:/project/target"
	@echo   make r-reflow-tags-convert-dryrun REMOTE_WORKSPACE="D:/project/target"
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
