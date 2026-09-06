# Aggregated help commands and module-loading order.

HELP_COMMANDS_LIST := help help-local help-docker help-compose help-remote
$(foreach cmd,$(HELP_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,HELP,$(cmd),)))

include make/core/help/variable.mk
include make/core/help/helper.mk
include make/core/setup_install/help.mk
include make/core/local/help.mk
include make/core/testing/help.mk
include make/core/lint_format/help.mk
include make/core/qa/help.mk
include make/core/ci/help.mk
include make/core/documentation/help.mk
include make/core/build_publish/help.mk
include make/core/docker/help.mk
include make/core/compose/help.mk
include make/core/remote/help.mk
include make/core/git/help.mk
include make/core/cleanup/help.mk
include make/core/variables/help.mk
include make/core/examples/help.mk

define HELP_CONTENT_LOCAL
	@$(MAKE) --no-print-directory help-setup-installation
	@$(MAKE) --no-print-directory help-local-init
	@$(MAKE) --no-print-directory help-local-scan
	@$(MAKE) --no-print-directory help-testing
	@$(MAKE) --no-print-directory help-lint-format
	@$(MAKE) --no-print-directory help-quality-assurance
	@$(MAKE) --no-print-directory help-ci
	@$(MAKE) --no-print-directory help-documentation
	@$(MAKE) --no-print-directory help-build-publish
	@$(MAKE) --no-print-directory help-git
	@$(MAKE) --no-print-directory help-cleanup-project
endef

define HELP_CONTENT_DOCKER
	@$(MAKE) --no-print-directory help-docker-build
	@$(MAKE) --no-print-directory help-docker-testing
	@$(MAKE) --no-print-directory help-docker-init
	@$(MAKE) --no-print-directory help-docker-scan
	@$(MAKE) --no-print-directory help-cleanup-docker
endef

define HELP_CONTENT_COMPOSE
	@$(MAKE) --no-print-directory help-compose-infrastructure
	@$(MAKE) --no-print-directory help-compose-init
	@$(MAKE) --no-print-directory help-compose-scan
	@$(MAKE) --no-print-directory help-compose-utilities
	@$(MAKE) --no-print-directory help-cleanup-docker
endef

define HELP_CONTENT_REMOTE
	@$(MAKE) --no-print-directory help-remote-phs-registry
	@$(MAKE) --no-print-directory help-remote-phs-runtime
	@$(MAKE) --no-print-directory help-remote-docgen-registry
	@$(MAKE) --no-print-directory help-remote-docgen-runtime
	@$(MAKE) --no-print-directory help-remote-custy-registry
	@$(MAKE) --no-print-directory help-remote-custy-runtime
	@$(MAKE) --no-print-directory help-remote-reflow-registry
	@$(MAKE) --no-print-directory help-remote-reflow-runtime
endef

define HELP_START
	@$(MAKE) --no-print-directory help-header
	@$(MAKE) --no-print-directory help-help
endef

define HELP_END
	@$(MAKE) --no-print-directory help-variables
	@$(MAKE) --no-print-directory help-examples
	@$(MAKE) --no-print-directory help-footer GROUP=$(1)
endef

.PHONY: help-local help-docker help-compose help-remote help
help-local:
	$(HELP_START)
	$(HELP_CONTENT_LOCAL)
	$(call HELP_END,LOCAL)
help-docker:
	$(HELP_START)
	$(HELP_CONTENT_DOCKER)
	$(call HELP_END,DOCKER)
help-compose:
	$(HELP_START)
	$(HELP_CONTENT_COMPOSE)
	$(call HELP_END,COMPOSE)
help-remote:
	$(HELP_START)
	$(HELP_CONTENT_REMOTE)
	$(call HELP_END,REMOTE)
help:
	$(HELP_START)
	$(HELP_CONTENT_LOCAL)
	$(HELP_CONTENT_DOCKER)
	$(HELP_CONTENT_COMPOSE)
	$(HELP_CONTENT_REMOTE)
	$(call HELP_END,ALL)
