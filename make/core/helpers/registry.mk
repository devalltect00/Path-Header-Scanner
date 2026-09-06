# Command registration helpers used to generate accurate grouped help output.

define REGISTER_COMMAND
$(eval $(1)_COMMANDS += $(2))
$(foreach group,$(3),$(eval $(group)_COMMANDS += $(2)))
$(eval ALL_COMMANDS += $(2))
endef

COMMAND_COUNT = $(words $($(1)_COMMANDS))
