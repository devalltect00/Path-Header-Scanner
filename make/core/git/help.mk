# Help for read-only Git utilities.

.PHONY: help-git
help-git:
	@echo [Git Utilities] $(call HELP_TOTAL,GIT)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make git-current-branch             $(HELP_COLUMN_SEPARATOR)    Show the current branch
	@echo   make git-url-origin                 $(HELP_COLUMN_SEPARATOR)    Show the origin URL
	@echo   make git-log                        $(HELP_COLUMN_SEPARATOR)    Show recent decorated history
	@echo   make git-tags                       $(HELP_COLUMN_SEPARATOR)    Show commits referenced by tags
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
