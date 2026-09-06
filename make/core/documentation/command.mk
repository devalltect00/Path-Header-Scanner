# MkDocs development and build workflows.

DOCUMENTATION_COMMANDS_LIST := docs-serve docs-build
$(foreach cmd,$(DOCUMENTATION_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,DOCUMENTATION,$(cmd),LOCAL)))

.PHONY: docs-serve docs-build
docs-serve: check-venv
	"$(PYTHON)" -m $(MKDOCS) serve

docs-build: check-venv
	"$(PYTHON)" -m $(MKDOCS) build
