# Header, footer, and help-index targets shared by grouped help commands.

.PHONY: help-header help-footer help-help
help-header:
	@$(ECHO_BLANK)
	@echo $(HELP_HEADER)
	@echo  $(DISPLAY_NAME) - Available Commands
	@echo $(HELP_HEADER)
	@$(ECHO_BLANK)

help-footer:
ifeq ($(GROUP),ALL)
	@echo Total Commands: $(call COMMAND_COUNT,ALL)
else
	@echo Commands in $(GROUP_DISPLAY_$(GROUP)): $(call COMMAND_COUNT,$(GROUP))
endif
	@$(ECHO_BLANK)
	@echo $(HELP_HEADER)

help-help:
	@echo [Help] $(call HELP_TOTAL,HELP)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make help                           $(HELP_COLUMN_SEPARATOR)    Show all available commands
	@echo   make help-local                     $(HELP_COLUMN_SEPARATOR)    Show local development commands
	@echo   make help-docker                    $(HELP_COLUMN_SEPARATOR)    Show Docker commands
	@echo   make help-compose                   $(HELP_COLUMN_SEPARATOR)    Show Docker Compose commands
	@echo   make help-remote                    $(HELP_COLUMN_SEPARATOR)    Show remote service commands
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
