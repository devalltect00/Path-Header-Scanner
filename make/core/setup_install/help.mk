# Help for Python environment and dependency setup.

.PHONY: help-setup-installation
help-setup-installation:
	@echo [Setup and Installation] $(call HELP_TOTAL,SETUP_INSTALL)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make venv                           $(HELP_COLUMN_SEPARATOR)    Create the Python 3.14+ virtual environment
	@echo   make activate                       $(HELP_COLUMN_SEPARATOR)    Show activation commands
	@echo   make install                        $(HELP_COLUMN_SEPARATOR)    Install Reflow in editable mode
	@echo   make install-dev                    $(HELP_COLUMN_SEPARATOR)    Install development dependencies
	@echo   make install-docs                   $(HELP_COLUMN_SEPARATOR)    Install documentation dependencies
	@echo   make install-all                    $(HELP_COLUMN_SEPARATOR)    Install development and documentation dependencies
	@echo   make upgrade-pip                    $(HELP_COLUMN_SEPARATOR)    Upgrade pip in the virtual environment
	@echo   make requirements                   $(HELP_COLUMN_SEPARATOR)    Regenerate requirements.txt
	@echo   make pre-commit-install             $(HELP_COLUMN_SEPARATOR)    Install the pre-commit Git hook
	@echo   make pre-commit-install-hooks       $(HELP_COLUMN_SEPARATOR)    Install the Git hook and hook environments
	@echo   make pre-commit-run                 $(HELP_COLUMN_SEPARATOR)    Run all hooks against all repository files
	@echo   make pre-commit-run-staged          $(HELP_COLUMN_SEPARATOR)    Run hooks against currently staged files
	@echo   make pre-commit-update              $(HELP_COLUMN_SEPARATOR)    Update hook revisions in the pre-commit config
	@echo   make pre-commit-clean               $(HELP_COLUMN_SEPARATOR)    Remove cached pre-commit hook environments
	@echo   make pre-commit-gc                  $(HELP_COLUMN_SEPARATOR)    Remove unused pre-commit cached repositories
	@echo   make pre-commit-uninstall           $(HELP_COLUMN_SEPARATOR)    Remove the pre-commit Git hook
	@echo   make pre-commit-validate            $(HELP_COLUMN_SEPARATOR)    Validate .pre-commit-config.yaml
	@echo   make pre-commit-refresh             $(HELP_COLUMN_SEPARATOR)    Update, clean, reinstall, and run all pre-commit hooks
	@echo   make setup                          $(HELP_COLUMN_SEPARATOR)    Create the environment and install all developer tooling
	@echo   make check-python                   $(HELP_COLUMN_SEPARATOR)    Validate and display the system Python version
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
