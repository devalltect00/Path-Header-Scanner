# Docker Compose image and stack lifecycle commands.

COMPOSE_INFRASTRUCTURE_COMMANDS_LIST := \
	c-build-base c-build-dev c-build-prod c-build-all \
	c-up c-up-build c-up-detached c-down c-down-clean c-logs

$(foreach cmd,$(COMPOSE_INFRASTRUCTURE_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,COMPOSE_INFRASTRUCTURE,$(cmd),COMPOSE)))

.PHONY: c-build-base c-build-dev c-build-prod c-build-all
c-build-base: docker-check
	$(COMPOSE_BASE) build base

c-build-dev: c-build-base
	$(COMPOSE_DEV) build $(SERVICE_APP)

c-build-prod: c-build-base
	$(COMPOSE_PROD) build $(SERVICE_APP)

c-build-all: docker-check
	$(COMPOSE_BASE) build base
	$(COMPOSE_DEV) build $(SERVICE_APP)
	$(COMPOSE_PROD) build $(SERVICE_APP)

.PHONY: c-up c-up-build c-up-detached c-down c-down-clean c-logs
c-up: docker-check
	$(COMPOSE_DEV) up

c-up-build: docker-check
	$(COMPOSE_DEV) up --build

c-up-detached: docker-check
	$(COMPOSE_DEV) up -d

c-down: docker-check
	$(COMPOSE_DEV) down

c-down-clean: docker-check
	$(COMPOSE_DEV) down -v --remove-orphans

c-logs: docker-check
	$(COMPOSE_DEV) logs -f
