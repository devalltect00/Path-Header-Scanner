# Shared formatting values for Custy-style Make help output.

HELP_SEPARATOR := ----------------------------------------------------------------------------------------------------
HELP_HEADER := =========================================================

ifeq ($(PLATFORM),windows)
	HELP_COLUMN_SEPARATOR := ^|
	HELP_TOTAL_OPEN := (
	HELP_TOTAL_CLOSE := )
else
	HELP_COLUMN_SEPARATOR := \|
	HELP_TOTAL_OPEN := \(
	HELP_TOTAL_CLOSE := \)
endif

HELP_TOTAL = $(HELP_TOTAL_OPEN)Total: $(call COMMAND_COUNT,$(1))$(HELP_TOTAL_CLOSE)

GROUP_DISPLAY_LOCAL := Local Development
GROUP_DISPLAY_DOCKER := Docker
GROUP_DISPLAY_COMPOSE := Docker Compose
GROUP_DISPLAY_REMOTE := Remote Services
GROUP_DISPLAY_ALL := All Commands
