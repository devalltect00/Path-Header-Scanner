# Project and Docker cleanup commands.

PROJECT_CLEANUP_COMMANDS_LIST := \
	clean-cache clean-build clean-pyc clean-coverage clean-pytest-tmp clean-pip-cache clean-venv clean clean-all
DOCKER_CLEANUP_COMMANDS_LIST := d-remove-images d-prune d-prune-all

$(foreach cmd,$(PROJECT_CLEANUP_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,PROJECT_CLEANUP,$(cmd),LOCAL)))
$(foreach cmd,$(DOCKER_CLEANUP_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,DOCKER_CLEANUP,$(cmd),DOCKER COMPOSE)))

.PHONY: clean-cache
clean-cache:
	$(call REQUIRE_PYTHON)
	@"$(PYTHON_SYSTEM)" -c "import shutil; [shutil.rmtree(path, ignore_errors=True) for path in ('.pytest_cache', '.ruff_cache', '.mypy_cache')]"
	@echo Tool caches removed.

.PHONY: clean-build
clean-build:
	$(call REQUIRE_PYTHON)
	@"$(PYTHON_SYSTEM)" -c "from pathlib import Path; import shutil; [shutil.rmtree(path, ignore_errors=True) for path in ('build', 'dist', 'site', 'htmlcov')]; [shutil.rmtree(path, ignore_errors=True) for path in Path('.').glob('*.egg-info')]"
	@echo Build artifacts removed.

.PHONY: clean-pyc
clean-pyc:
	$(call REQUIRE_PYTHON)
	@"$(PYTHON_SYSTEM)" -c "from pathlib import Path; import shutil; [path.unlink(missing_ok=True) for path in Path('.').rglob('*.pyc')]; [shutil.rmtree(path, ignore_errors=True) for path in Path('.').rglob('__pycache__')]"
	@echo Python caches removed.

.PHONY: clean-coverage
clean-coverage:
	$(call REQUIRE_PYTHON)
	@"$(PYTHON_SYSTEM)" -c "from pathlib import Path; import shutil; Path('.coverage').unlink(missing_ok=True); shutil.rmtree('htmlcov', ignore_errors=True)"
	@echo Coverage artifacts removed.

# 🧹 CLEANUP - PYTEST TEMP DIRECTORIES
.PHONY: clean-pytest-tmp
clean-pytest-tmp:
	$(call REQUIRE_PYTHON)
	@echo Cleaning pytest temporary directories...
	@$(PYTHON_SYSTEM) -c "import pathlib, shutil; \
[shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').glob('.pytest-tmp-*') if p.is_dir()]"
	@echo Pytest temporary directories cleanup completed.

.PHONY: clean-pip-cache
clean-pip-cache:
	$(call REQUIRE_PYTHON)
	@"$(PYTHON_SYSTEM)" -m pip cache purge

.PHONY: clean-venv
clean-venv:
	$(call REQUIRE_PYTHON)
	@"$(PYTHON_SYSTEM)" -c "from pathlib import Path; import shutil; root=Path.cwd().resolve(); target=(root / '$(VENV_NAME)').resolve(); assert target.parent == root and target != root, 'Refusing unsafe virtual-environment path'; shutil.rmtree(target, ignore_errors=True)"
	@echo Virtual environment removed: $(VENV_NAME)

.PHONY: clean clean-all
clean: clean-cache clean-build clean-pyc clean-coverage clean-pytest-tmp
	@echo Standard project cleanup completed.

clean-all: clean clean-venv
	@echo Full project cleanup completed.

.PHONY: d-remove-images d-prune d-prune-all
d-remove-images: docker-check
	-$(DOCKER) rmi $(DOCKER_IMAGE_BASE)
	-$(DOCKER) rmi $(DOCKER_IMAGE_DEV)
	-$(DOCKER) rmi $(DOCKER_IMAGE_PROD)

d-prune: docker-check
	$(DOCKER) system prune -f

d-prune-all: docker-check
	$(DOCKER) system prune -a -f --volumes
