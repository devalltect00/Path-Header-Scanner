# Path Header Scanner commands executed from the project virtual environment.

LOCAL_INIT_COMMANDS_LIST := l-init l-init-force l-init-ask l-init-all l-init-config
LOCAL_SCAN_COMMANDS_LIST := l-scan l-scan-apply l-scan-debug l-scan-apply-debug l-scan-apply-all

$(foreach cmd,$(LOCAL_INIT_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,LOCAL_INIT,$(cmd),LOCAL)))
$(foreach cmd,$(LOCAL_SCAN_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,LOCAL_SCAN,$(cmd),LOCAL)))

.PHONY: l-init l-init-force l-init-ask l-init-all l-init-config
l-init: check-venv
	$(LOCAL_RUN) $(LOCAL_PHS_GLOBAL_ARGS) init $(LOCAL_PHS_INIT_ARGS) $(LOCAL_PHS_EXTRA_ARGS)

l-init-force: override LOCAL_PHS_INIT_ARGS += --force
l-init-force: l-init

l-init-ask: override LOCAL_PHS_INIT_ARGS += --ask
l-init-ask: l-init

l-init-all: override LOCAL_PHS_INIT_ARGS += --mode all
l-init-all: l-init

l-init-config: override LOCAL_PHS_INIT_ARGS += --mode config
l-init-config: l-init

.PHONY: l-scan l-scan-apply l-scan-debug l-scan-apply-debug l-scan-apply-all
l-scan: check-venv
	$(LOCAL_RUN) $(LOCAL_PHS_GLOBAL_ARGS) scan $(TARGET) $(LOCAL_PHS_SCAN_ARGS) $(LOCAL_PHS_EXTRA_ARGS)

l-scan-apply: override LOCAL_PHS_SCAN_ARGS += --apply
l-scan-apply: l-scan

l-scan-debug: override LOCAL_PHS_SCAN_ARGS += --debug
l-scan-debug: l-scan

l-scan-apply-debug: override LOCAL_PHS_SCAN_ARGS += --apply --debug
l-scan-apply-debug: l-scan

l-scan-apply-all:
ifeq ($(PLATFORM),windows)
	@for %%t in ($(PHS_SCAN_TARGETS)) do ( \
		$(MAKE) --no-print-directory l-scan-apply \
			TARGET=%%t \
			LOCAL_PHS_GLOBAL_ARGS="$(LOCAL_PHS_GLOBAL_ARGS)" \
			LOCAL_PHS_SCAN_ARGS="$(LOCAL_PHS_SCAN_ARGS)" \
			LOCAL_PHS_EXTRA_ARGS="$(LOCAL_PHS_EXTRA_ARGS)" \
	)
else
	@for target in $(PHS_SCAN_TARGETS); do \
		$(MAKE) --no-print-directory l-scan-apply \
			TARGET="$$target" \
			LOCAL_PHS_GLOBAL_ARGS="$(LOCAL_PHS_GLOBAL_ARGS)" \
			LOCAL_PHS_SCAN_ARGS="$(LOCAL_PHS_SCAN_ARGS)" \
			LOCAL_PHS_EXTRA_ARGS="$(LOCAL_PHS_EXTRA_ARGS)"; \
	done
endif
