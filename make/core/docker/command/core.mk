# Path Header Scanner and test commands executed in local Docker images.

DOCKER_TESTING_COMMANDS_LIST := d-test
DOCKER_INIT_COMMANDS_LIST := d-init d-init-force d-init-ask d-init-all d-init-config
DOCKER_SCAN_COMMANDS_LIST := d-scan d-scan-apply d-scan-debug d-scan-apply-debug d-scan-apply-all

$(foreach cmd,$(DOCKER_TESTING_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,DOCKER_TESTING,$(cmd),DOCKER)))
$(foreach cmd,$(DOCKER_INIT_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,DOCKER_INIT,$(cmd),DOCKER)))
$(foreach cmd,$(DOCKER_SCAN_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,DOCKER_SCAN,$(cmd),DOCKER)))

.PHONY: d-test
d-test: d-build-dev
	$(DOCKER_RUN_NO_ENTRYPOINT) $(DOCKER_WORKSPACE) $(DOCKER_IMAGE_DEV) python -m pytest -v

.PHONY: d-init d-init-force d-init-ask d-init-all d-init-config
d-init: docker-check
	$(DOCKER_RUN_INTERACTIVE) $(DOCKER_WORKSPACE) $(DOCKER_IMAGE_PROD) $(DOCKER_PHS_GLOBAL_ARGS) init $(DOCKER_PHS_INIT_ARGS) $(DOCKER_PHS_EXTRA_ARGS)

d-init-force: override DOCKER_PHS_INIT_ARGS += --force
d-init-force: d-init

d-init-ask: override DOCKER_PHS_INIT_ARGS += --ask
d-init-ask: d-init

d-init-all: override DOCKER_PHS_INIT_ARGS += --mode all
d-init-all: d-init

d-init-config: override DOCKER_PHS_INIT_ARGS += --mode config
d-init-config: d-init

.PHONY: d-scan d-scan-apply d-scan-debug d-scan-apply-debug d-scan-apply-all
d-scan: docker-check
	$(DOCKER_RUN_INTERACTIVE) $(DOCKER_WORKSPACE) $(DOCKER_IMAGE_PROD) $(DOCKER_PHS_GLOBAL_ARGS) scan $(TARGET) $(DOCKER_PHS_SCAN_ARGS) $(DOCKER_PHS_EXTRA_ARGS)

d-scan-apply: override DOCKER_PHS_SCAN_ARGS += --apply
d-scan-apply: d-scan

d-scan-debug: override DOCKER_PHS_SCAN_ARGS += --debug
d-scan-debug: d-scan

d-scan-apply-debug: override DOCKER_PHS_SCAN_ARGS += --apply --debug
d-scan-apply-debug: d-scan

d-scan-apply-all:
ifeq ($(PLATFORM),windows)
	@for %%t in ($(PHS_SCAN_TARGETS)) do ( \
		$(MAKE) --no-print-directory d-scan-apply \
			TARGET=%%t \
			DOCKER_PHS_GLOBAL_ARGS="$(DOCKER_PHS_GLOBAL_ARGS)" \
			DOCKER_PHS_SCAN_ARGS="$(DOCKER_PHS_SCAN_ARGS)" \
			DOCKER_PHS_EXTRA_ARGS="$(DOCKER_PHS_EXTRA_ARGS)" \
	)
else
	@for target in $(PHS_SCAN_TARGETS); do \
		$(MAKE) --no-print-directory d-scan-apply \
			TARGET="$$target" \
			DOCKER_PHS_GLOBAL_ARGS="$(DOCKER_PHS_GLOBAL_ARGS)" \
			DOCKER_PHS_SCAN_ARGS="$(DOCKER_PHS_SCAN_ARGS)" \
			DOCKER_PHS_EXTRA_ARGS="$(DOCKER_PHS_EXTRA_ARGS)"; \
	done
endif
