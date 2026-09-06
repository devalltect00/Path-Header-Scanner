# Local Docker image build commands.

DOCKER_INFRASTRUCTURE_COMMANDS_LIST := d-build-base d-build-dev d-build-prod d-build-all
$(foreach cmd,$(DOCKER_INFRASTRUCTURE_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,DOCKER_INFRASTRUCTURE,$(cmd),DOCKER)))

.PHONY: docker-check
docker-check:
	$(call REQUIRE_DOCKER)
	@echo Docker is ready.

.PHONY: d-build-base d-build-dev d-build-prod d-build-all
d-build-base: docker-check
	$(DOCKER) build -f $(DOCKERFILE_BASE) --target base -t $(DOCKER_IMAGE_BASE) .

d-build-dev: d-build-base
	$(DOCKER) build -f $(DOCKERFILE_BASE) --target development -t $(DOCKER_IMAGE_DEV) .

d-build-prod: d-build-base
	$(DOCKER) build -f $(DOCKERFILE_BASE) --target production -t $(DOCKER_IMAGE_PROD) .

d-build-all: docker-check
	$(DOCKER) build -f $(DOCKERFILE_BASE) --target base -t $(DOCKER_IMAGE_BASE) .
	$(DOCKER) build -f $(DOCKERFILE_BASE) --target development -t $(DOCKER_IMAGE_DEV) .
	$(DOCKER) build -f $(DOCKERFILE_BASE) --target production -t $(DOCKER_IMAGE_PROD) .
