# Help for project and Docker cleanup commands.

.PHONY: help-cleanup-project help-cleanup-docker
help-cleanup-project:
	@echo [Project Cleanup] $(call HELP_TOTAL,PROJECT_CLEANUP)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make clean-cache                    $(HELP_COLUMN_SEPARATOR)    Remove tool caches
	@echo   make clean-build                    $(HELP_COLUMN_SEPARATOR)    Remove build, docs, and coverage output directories
	@echo   make clean-pyc                      $(HELP_COLUMN_SEPARATOR)    Remove Python bytecode caches
	@echo   make clean-coverage                 $(HELP_COLUMN_SEPARATOR)    Remove coverage output
	@echo   make clean-pytest-tmp               $(HELP_COLUMN_SEPARATOR)    Remove pytest temporary directories
	@echo   make clean-pip-cache                $(HELP_COLUMN_SEPARATOR)    Purge the pip download cache
	@echo   make clean-venv                     $(HELP_COLUMN_SEPARATOR)    Remove the configured virtual environment
	@echo   make clean                          $(HELP_COLUMN_SEPARATOR)    Remove standard generated project artifacts
	@echo   make clean-all                      $(HELP_COLUMN_SEPARATOR)    Run clean and remove the virtual environment
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-cleanup-docker:
	@echo [Docker Cleanup] $(call HELP_TOTAL,DOCKER_CLEANUP)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make d-remove-images                $(HELP_COLUMN_SEPARATOR)    Remove local Path Header Scanner images
	@echo   make d-prune                        $(HELP_COLUMN_SEPARATOR)    Remove unused Docker resources
	@echo   make d-prune-all                    $(HELP_COLUMN_SEPARATOR)    Remove all unused Docker resources and volumes
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
