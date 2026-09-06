# Path Header Scanner development and runtime automation.
#
# The root file intentionally contains only the module loading order. Command
# implementations live under make/core so each workflow can evolve separately.

.DEFAULT_GOAL := help

ROOT_DIR := $(CURDIR)

# Relative include paths support repository paths containing spaces. Use a
# current GNU Make 4.x release and run it from the repository root.
include make/core/variables/variable.mk
include make/core/helpers/common.mk
include make/core/helpers/registry.mk

include make/core/setup_install/command.mk
include make/core/local/command.mk
include make/core/testing/command.mk
include make/core/lint_format/command.mk
include make/core/qa/command.mk
include make/core/ci/command.mk
include make/core/documentation/command.mk
include make/core/build_publish/command.mk
include make/core/docker/command/common.mk
include make/core/docker/command/core.mk
include make/core/compose/command/common.mk
include make/core/compose/command/core.mk
include make/core/remote/command/registry.mk
include make/core/remote/command/runtime.mk
include make/core/git/command.mk
include make/core/cleanup/command.mk

include make/core/help/command.mk
