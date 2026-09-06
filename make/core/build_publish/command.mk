# Python package build and publication workflows.

BUILD_PUBLISH_COMMANDS_LIST := build publish build-all
$(foreach cmd,$(BUILD_PUBLISH_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,BUILD_PUBLISH,$(cmd),LOCAL)))

.PHONY: validate-package-resources
validate-package-resources: docker-check
	$(DOCKER) run --rm --entrypoint python $(DOCKER_IMAGE_PROD) -c "from importlib.resources import files; resource=files('$(PROJECT_PACKAGE).templates').joinpath('config.toml'); assert resource.is_file(); print('OK')"

.PHONY: build publish build-all
build: check-venv clean-cache
	"$(PYTHON)" -m $(BUILD)

publish: check-venv
	"$(PYTHON)" -m $(TWINE) upload dist/*

build-all: build d-build-all
