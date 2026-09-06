# Path Header Scanner and developer commands executed through Docker Compose.

COMPOSE_INIT_COMMANDS_LIST := c-init c-init-force c-init-ask c-init-all c-init-config
COMPOSE_SCAN_COMMANDS_LIST := c-scan c-scan-apply c-scan-debug c-scan-apply-debug c-scan-apply-all
COMPOSE_UTILITIES_COMMANDS_LIST := c-test c-lint c-lint-fix c-format c-format-check c-docs c-shell c-build-package c-exec-shell c-fix c-check c-qa c-ci

$(foreach cmd,$(COMPOSE_INIT_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,COMPOSE_INIT,$(cmd),COMPOSE)))
$(foreach cmd,$(COMPOSE_SCAN_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,COMPOSE_SCAN,$(cmd),COMPOSE)))
$(foreach cmd,$(COMPOSE_UTILITIES_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,COMPOSE_UTILITIES,$(cmd),COMPOSE)))

.PHONY: c-init c-init-force c-init-ask c-init-all c-init-config
c-init: docker-check
	$(COMPOSE_PROD_RUN_APP) $(COMPOSE_PHS_GLOBAL_ARGS) init $(COMPOSE_PHS_INIT_ARGS) $(COMPOSE_PHS_EXTRA_ARGS)

c-init-force: override COMPOSE_PHS_INIT_ARGS += --force
c-init-force: c-init

c-init-ask: override COMPOSE_PHS_INIT_ARGS += --ask
c-init-ask: c-init

c-init-all: override COMPOSE_PHS_INIT_ARGS += --mode all
c-init-all: c-init

c-init-config: override COMPOSE_PHS_INIT_ARGS += --mode config
c-init-config: c-init

.PHONY: c-scan c-scan-apply c-scan-debug c-scan-apply-debug c-scan-apply-all
c-scan: docker-check
	$(COMPOSE_PROD_RUN_APP) $(COMPOSE_PHS_GLOBAL_ARGS) scan $(TARGET) $(COMPOSE_PHS_SCAN_ARGS) $(COMPOSE_PHS_EXTRA_ARGS)

c-scan-apply: override COMPOSE_PHS_SCAN_ARGS += --apply
c-scan-apply: c-scan

c-scan-debug: override COMPOSE_PHS_SCAN_ARGS += --debug
c-scan-debug: c-scan

c-scan-apply-debug: override COMPOSE_PHS_SCAN_ARGS += --apply --debug
c-scan-apply-debug: c-scan

c-scan-apply-all:
ifeq ($(PLATFORM),windows)
	@for %%t in ($(PHS_SCAN_TARGETS)) do ( \
		$(MAKE) --no-print-directory c-scan-apply \
			TARGET=%%t \
			COMPOSE_PHS_GLOBAL_ARGS="$(COMPOSE_PHS_GLOBAL_ARGS)" \
			COMPOSE_PHS_SCAN_ARGS="$(COMPOSE_PHS_SCAN_ARGS)" \
			COMPOSE_PHS_EXTRA_ARGS="$(COMPOSE_PHS_EXTRA_ARGS)" \
	)
else
	@for target in $(PHS_SCAN_TARGETS); do \
		$(MAKE) --no-print-directory c-scan-apply \
			TARGET="$$target" \
			COMPOSE_PHS_GLOBAL_ARGS="$(COMPOSE_PHS_GLOBAL_ARGS)" \
			COMPOSE_PHS_SCAN_ARGS="$(COMPOSE_PHS_SCAN_ARGS)" \
			COMPOSE_PHS_EXTRA_ARGS="$(COMPOSE_PHS_EXTRA_ARGS)"; \
	done
endif

.PHONY: c-test c-lint c-lint-fix c-format c-format-check c-docs c-shell c-build-package c-exec-shell
c-test: c-build-dev
	$(COMPOSE_DEV_RUN_TEST)
c-lint: c-build-dev
	$(COMPOSE_DEV_RUN_LINT)
c-lint-fix: c-build-dev
	$(COMPOSE_DEV_RUN_LINT_FIX)
c-format: c-build-dev
	$(COMPOSE_DEV_RUN_FORMAT)
c-format-check: c-build-dev
	$(COMPOSE_DEV_RUN_FORMAT_CHECK)
c-docs: docker-check
	$(COMPOSE_DEV_UP_DOCS) -d
c-shell: c-build-dev
	$(COMPOSE_DEV_RUN_SHELL)
c-build-package: c-build-dev
	$(COMPOSE_DEV_RUN_BUILD)
c-exec-shell: docker-check
	$(COMPOSE_DEV_EXEC) $(SERVICE_APP) $(SHELL_BIN)

.PHONY: c-fix c-check c-qa c-ci
c-fix: docker-check
	@$(MAKE) --no-print-directory c-format
	@$(MAKE) --no-print-directory c-lint-fix
c-check: docker-check
	@$(MAKE) --no-print-directory c-format-check
	@$(MAKE) --no-print-directory c-lint
	@$(MAKE) --no-print-directory c-test
c-qa: docker-check
	@$(MAKE) --no-print-directory c-fix
	@$(MAKE) --no-print-directory c-check
c-ci: docker-check
	@$(MAKE) --no-print-directory c-build-dev
	@$(MAKE) --no-print-directory c-check
