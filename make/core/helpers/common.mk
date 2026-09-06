# Shared validation and remote-container helper macros.

define REQUIRE_DOCKER
	@$(DOCKER) --version >$(NULL_DEVICE) 2>&1 || (echo Docker is not installed. && exit 1)
	@$(DOCKER) info >$(NULL_DEVICE) 2>&1 || (echo Docker is installed but not running. && exit 1)
endef

define REQUIRE_PYTHON
	@"$(PYTHON_SYSTEM)" --version >$(NULL_DEVICE) 2>&1 || (echo Python is not installed. && exit 1)
	@"$(PYTHON_SYSTEM)" -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 14) else 'Python 3.14+ is required.')"
endef

define REQUIRE_REMOTE
	$(call REQUIRE_DOCKER)
endef

define REQUIRE_REMOTE_PUSH
	$(call REQUIRE_DOCKER)
endef

define REMOTE_IMAGE_FULL
$(GHCR_REGISTRY)/$(GHCR_OWNER)/$($(1)):$(REMOTE_TAG)
endef

define ENSURE_REMOTE_IMAGE
	@$(DOCKER) image inspect $(call REMOTE_IMAGE_FULL,$(1)) >$(NULL_DEVICE) 2>&1 || ($(DOCKER) pull $(call REMOTE_IMAGE_FULL,$(1)))
endef

define PULL_REMOTE_IMAGE
	$(DOCKER) pull $(call REMOTE_IMAGE_FULL,$(1))
endef

define PUSH_REMOTE_IMAGE
	$(DOCKER) push $(call REMOTE_IMAGE_FULL,$(1))
endef

define REMOVE_REMOTE_IMAGE
	$(DOCKER) image rm $(call REMOTE_IMAGE_FULL,$(1))
endef

define REMOTE_RUN
$(DOCKER_RUN_INTERACTIVE) $(DOCKER_REMOTE_WORKSPACE) $(call REMOTE_IMAGE_FULL,$(1))
endef

define PRINT_REMOTE_INFO
	@echo Image: $($(1))
	@echo Tag: $(REMOTE_TAG)
	@echo Full: $(call REMOTE_IMAGE_FULL,$(1))
endef
