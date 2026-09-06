# Help for package build and publication commands.

.PHONY: help-build-publish
help-build-publish:
	@echo [Build and Publish] $(call HELP_TOTAL,BUILD_PUBLISH)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make build                          $(HELP_COLUMN_SEPARATOR)    Build Python package artifacts
	@echo   make publish                        $(HELP_COLUMN_SEPARATOR)    Upload dist artifacts with Twine
	@echo   make build-all                      $(HELP_COLUMN_SEPARATOR)    Build Python and Docker artifacts
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
