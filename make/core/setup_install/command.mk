# Python environment, dependency installation, and developer setup commands.

SETUP_INSTALL_COMMANDS_LIST := \
	venv activate install install-dev install-docs install-all upgrade-pip \
	requirements pre-commit-install pre-commit-install-hooks pre-commit-run \
	pre-commit-run-staged pre-commit-update pre-commit-clean pre-commit-gc \
	pre-commit-uninstall pre-commit-validate pre-commit-refresh setup check-python

$(foreach cmd,$(SETUP_INSTALL_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,SETUP_INSTALL,$(cmd),LOCAL)))

.PHONY: check-venv
check-venv:
ifeq ($(PLATFORM),windows)
	@if not exist "$(PYTHON)" (echo Virtual environment not found. Run 'make venv' first. && exit 1)
else
	@test -f "$(PYTHON)" || (echo "Virtual environment not found. Run 'make venv' first."; exit 1)
endif

.PHONY: venv
venv:
	$(call REQUIRE_PYTHON)
	"$(PYTHON_SYSTEM)" -m venv "$(VENV_NAME)"
	@echo Virtual environment created: $(VENV_NAME)

.PHONY: activate
activate:
	@echo Activation commands
ifeq ($(PLATFORM),windows)
	@echo CMD: $(ACTIVATE_COMMAND)
	@echo PowerShell: $(ACTIVATE_COMMAND_PS)
else
	@echo $(ACTIVATE_COMMAND)
endif

.PHONY: install install-dev install-docs install-all
install: check-venv
	"$(PIP)" install -e .

install-dev: check-venv
	"$(PIP)" install -e ".[dev]"

install-docs: check-venv
	"$(PIP)" install -e ".[docs]"

install-all: check-venv
	"$(PIP)" install -e ".[dev,docs]"

.PHONY: upgrade-pip
upgrade-pip: check-venv
	"$(PIP)" install --upgrade pip

.PHONY: requirements
requirements: check-venv
	@echo Generating requirements.txt from the active Reflow virtual environment...
	@"$(PYTHON)" -c "import subprocess; prefixes=tuple('$(REQUIREMENTS_EXCLUDE_PREFIXES)'.split()); req=subprocess.check_output([r'$(PIP)', 'freeze'], text=True); filtered='\n'.join(line for line in req.splitlines() if not line.startswith(prefixes) and not line.lstrip().startswith('# Editable install')); open('requirements.txt', 'w').write(filtered + '\n')"
	@echo requirements.txt generated successfully.

.PHONY: \
	pre-commit-install \
	pre-commit-install-hooks \
	pre-commit-run \
	pre-commit-run-staged \
	pre-commit-update \
	pre-commit-clean \
	pre-commit-gc \
	pre-commit-uninstall \
	pre-commit-validate \
	pre-commit-refresh

pre-commit-install: check-venv
	"$(PYTHON)" -m $(PRE_COMMIT) install

pre-commit-install-hooks: check-venv
	"$(PYTHON)" -m $(PRE_COMMIT) install --install-hooks

pre-commit-run: check-venv
	"$(PYTHON)" -m $(PRE_COMMIT) run --all-files

pre-commit-run-staged: check-venv
	"$(PYTHON)" -m $(PRE_COMMIT) run

pre-commit-update: check-venv
	"$(PYTHON)" -m $(PRE_COMMIT) autoupdate

pre-commit-clean: check-venv
	"$(PYTHON)" -m $(PRE_COMMIT) clean

pre-commit-gc: check-venv
	"$(PYTHON)" -m $(PRE_COMMIT) gc

pre-commit-uninstall: check-venv
	"$(PYTHON)" -m $(PRE_COMMIT) uninstall

pre-commit-validate: check-venv
	"$(PYTHON)" -m $(PRE_COMMIT) validate-config .pre-commit-config.yaml

pre-commit-refresh: check-venv
	"$(PYTHON)" -m $(PRE_COMMIT) autoupdate
	"$(PYTHON)" -m $(PRE_COMMIT) clean
	"$(PYTHON)" -m $(PRE_COMMIT) install --install-hooks
	"$(PYTHON)" -m $(PRE_COMMIT) run --all-files

.PHONY: setup
setup: venv upgrade-pip install-all pre-commit-install
	@echo Reflow development setup completed successfully.

.PHONY: check-python
check-python:
	$(call REQUIRE_PYTHON)
	@"$(PYTHON_SYSTEM)" --version
