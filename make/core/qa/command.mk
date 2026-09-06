# Local quality-assurance aggregate workflows.

QA_COMMANDS_LIST := fix check qa ci
$(foreach cmd,$(QA_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,QA,$(cmd),LOCAL)))

.PHONY: fix check qa ci
fix: check-venv
	@$(MAKE) --no-print-directory format
	@$(MAKE) --no-print-directory lint-fix

check: check-venv
	@$(MAKE) --no-print-directory format-check
	@$(MAKE) --no-print-directory lint
	@$(MAKE) --no-print-directory test

qa:
	@$(MAKE) --no-print-directory fix
	@$(MAKE) --no-print-directory check

ci: c-ci
