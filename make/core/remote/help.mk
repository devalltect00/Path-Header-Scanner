# Help for published Devalltect utility images.

.PHONY: help-remote-phs-registry help-remote-phs-runtime
.PHONY: help-remote-docgen-registry help-remote-docgen-runtime
.PHONY: help-remote-custy-registry help-remote-custy-runtime
.PHONY: help-remote-reflow-registry help-remote-reflow-runtime
.PHONY: help-remote-registry help-remote-runtime

# Compatibility aggregators retained from the first modular Reflow Makefile.
help-remote-registry:
	@$(MAKE) --no-print-directory help-remote-phs-registry
	@$(MAKE) --no-print-directory help-remote-docgen-registry
	@$(MAKE) --no-print-directory help-remote-custy-registry
	@$(MAKE) --no-print-directory help-remote-reflow-registry

help-remote-runtime:
	@$(MAKE) --no-print-directory help-remote-phs-runtime
	@$(MAKE) --no-print-directory help-remote-docgen-runtime
	@$(MAKE) --no-print-directory help-remote-custy-runtime
	@$(MAKE) --no-print-directory help-remote-reflow-runtime

help-remote-phs-registry:
	@echo [Remote - Path Header Scanner Registry] $(call HELP_TOTAL,REMOTE_PHS_REGISTRY)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make r-phs-info                     $(HELP_COLUMN_SEPARATOR)    Show remote image information
	@echo   make r-phs-pull                     $(HELP_COLUMN_SEPARATOR)    Pull remote image from registry
	@echo   make r-phs-push                     $(HELP_COLUMN_SEPARATOR)    Push remote image to registry
	@echo   make r-phs-remove                   $(HELP_COLUMN_SEPARATOR)    Remove local copy of remote image
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-remote-phs-runtime:
	@echo [Remote - Path Header Scanner Runtime] $(call HELP_TOTAL,REMOTE_PHS_RUNTIME)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make r-phs-init                     $(HELP_COLUMN_SEPARATOR)    Run initialization from remote image
	@echo   make r-phs-init-all                 $(HELP_COLUMN_SEPARATOR)    Initialize all resources
	@echo   make r-phs-init-force               $(HELP_COLUMN_SEPARATOR)    Initialize and overwrite files
	@echo   make r-phs-init-ask                 $(HELP_COLUMN_SEPARATOR)    Initialize with confirmation prompts
	@$(ECHO_BLANK)
	@echo   make r-phs-scan                     $(HELP_COLUMN_SEPARATOR)    Run scanner using remote image
	@echo   make r-phs-scan-apply               $(HELP_COLUMN_SEPARATOR)    Run scanner and apply changes
	@echo   make r-phs-scan-debug               $(HELP_COLUMN_SEPARATOR)    Run scanner in debug mode
	@echo   make r-phs-scan-apply-debug         $(HELP_COLUMN_SEPARATOR)    Apply changes and enable debug mode
	@echo   make r-phs-scan-apply-all           $(HELP_COLUMN_SEPARATOR)    Apply scanner to all configured targets
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-remote-docgen-registry:
	@echo [Remote - Doc Gen Registry] $(call HELP_TOTAL,REMOTE_DOC_GEN_REGISTRY)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make r-doc-gen-info                 $(HELP_COLUMN_SEPARATOR)    Show remote image information
	@echo   make r-doc-gen-pull                 $(HELP_COLUMN_SEPARATOR)    Pull remote image from registry
	@echo   make r-doc-gen-push                 $(HELP_COLUMN_SEPARATOR)    Push remote image to registry
	@echo   make r-doc-gen-remove               $(HELP_COLUMN_SEPARATOR)    Remove local copy of remote image
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-remote-docgen-runtime:
	@echo [Remote - Doc Gen Runtime] $(call HELP_TOTAL,REMOTE_DOC_GEN_RUNTIME)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make r-doc-init                     $(HELP_COLUMN_SEPARATOR)    Run initialization from remote image
	@echo   make r-doc-init-all                 $(HELP_COLUMN_SEPARATOR)    Initialize all resources
	@echo   make r-doc-init-force               $(HELP_COLUMN_SEPARATOR)    Initialize and overwrite files
	@echo   make r-doc-init-ask                 $(HELP_COLUMN_SEPARATOR)    Initialize with confirmation prompts
	@$(ECHO_BLANK)
	@echo   make r-doc-generate                 $(HELP_COLUMN_SEPARATOR)    Generate project documentation
	@echo   make r-doc-generate-smart           $(HELP_COLUMN_SEPARATOR)    Generate documentation using smart mode
	@echo   make r-doc-print                    $(HELP_COLUMN_SEPARATOR)    Print project structure
	@echo   make r-doc-print-smart              $(HELP_COLUMN_SEPARATOR)    Print project structure using smart mode
	@echo   make r-doc-analyze                  $(HELP_COLUMN_SEPARATOR)    Analyze project structure
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-remote-custy-registry:
	@echo [Remote - Custy Registry] $(call HELP_TOTAL,REMOTE_CUSTY_REGISTRY)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make r-custy-info                   $(HELP_COLUMN_SEPARATOR)    Show remote image information
	@echo   make r-custy-pull                   $(HELP_COLUMN_SEPARATOR)    Pull remote image from registry
	@echo   make r-custy-push                   $(HELP_COLUMN_SEPARATOR)    Push remote image to registry
	@echo   make r-custy-remove                 $(HELP_COLUMN_SEPARATOR)    Remove local copy of remote image
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-remote-custy-runtime:
	@echo [Remote - Custy Runtime] $(call HELP_TOTAL,REMOTE_CUSTY_RUNTIME)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make r-custy-init                   $(HELP_COLUMN_SEPARATOR)    Run initialization from remote image
	@echo   make r-custy-init-all               $(HELP_COLUMN_SEPARATOR)    Initialize all resources
	@echo   make r-custy-init-all-no-examples   $(HELP_COLUMN_SEPARATOR)    Initialize configuration and templates only
	@echo   make r-custy-init-config            $(HELP_COLUMN_SEPARATOR)    Initialize configuration files only
	@echo   make r-custy-init-templates         $(HELP_COLUMN_SEPARATOR)    Initialize templates only
	@echo   make r-custy-init-examples          $(HELP_COLUMN_SEPARATOR)    Initialize examples only
	@echo   make r-custy-init-force             $(HELP_COLUMN_SEPARATOR)    Initialize and overwrite files
	@echo   make r-custy-init-ask               $(HELP_COLUMN_SEPARATOR)    Initialize with confirmation prompts
	@$(ECHO_BLANK)
	@echo   make r-custy-credentials-set-github $(HELP_COLUMN_SEPARATOR)    Store a GitHub PAT using the remote image
	@echo   make r-custy-credentials-set-gitlab $(HELP_COLUMN_SEPARATOR)    Store a GitLab PAT using the remote image
	@echo   make r-custy-credentials-status     $(HELP_COLUMN_SEPARATOR)    Inspect mounted credential availability
	@echo   make r-custy-credentials-test       $(HELP_COLUMN_SEPARATOR)    Test read-only access to CUSTY_CREDENTIALS_REMOTE
	@$(ECHO_BLANK)
	@echo   make r-custy-run                    $(HELP_COLUMN_SEPARATOR)    Run remote command with custom arguments
	@echo   make r-custy-run-validate           $(HELP_COLUMN_SEPARATOR)    Run the validate command
	@echo   make r-custy-run-apply-version      $(HELP_COLUMN_SEPARATOR)    Run version update
	@echo   make r-custy-run-changelog          $(HELP_COLUMN_SEPARATOR)    Run changelog generate
	@echo   make r-custy-run-commit             $(HELP_COLUMN_SEPARATOR)    Create Git commit
	@echo   make r-custy-run-tag                $(HELP_COLUMN_SEPARATOR)    Create Git tag
	@echo   make r-custy-run-push               $(HELP_COLUMN_SEPARATOR)    Push commits and tags
	@echo   make r-custy-run-dev                $(HELP_COLUMN_SEPARATOR)    Run daily development workflow
	@echo   make r-custy-run-release            $(HELP_COLUMN_SEPARATOR)    Run release workflow
	@echo   make r-custy-run-full               $(HELP_COLUMN_SEPARATOR)    Run full workflow
	@$(ECHO_BLANK)
	@echo   make r-custy-run-backup-commit      $(HELP_COLUMN_SEPARATOR)    Backup commit message templates
	@echo   make r-custy-run-backup-tag         $(HELP_COLUMN_SEPARATOR)    Backup tag message templates
	@echo   make r-custy-run-backup-all         $(HELP_COLUMN_SEPARATOR)    Backup all templates
	@$(ECHO_BLANK)
	@echo   make r-custy-run-cleanup-backups    $(HELP_COLUMN_SEPARATOR)    Remove backup files
	@echo   make r-custy-run-cleanup-branches   $(HELP_COLUMN_SEPARATOR)    Remove temporary branches
	@echo   make r-custy-run-cleanup-all        $(HELP_COLUMN_SEPARATOR)    Run complete cleanup workflow
	@$(ECHO_BLANK)
	@echo   make r-custy-workflow               $(HELP_COLUMN_SEPARATOR)    Run experimental workflow branch command
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-remote-reflow-registry:
	@echo [Remote - Reflow Registry] $(call HELP_TOTAL,REMOTE_REFLOW_REGISTRY)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make r-reflow-info                  $(HELP_COLUMN_SEPARATOR)    Show remote image information
	@echo   make r-reflow-pull                  $(HELP_COLUMN_SEPARATOR)    Pull remote image from registry
	@echo   make r-reflow-push                  $(HELP_COLUMN_SEPARATOR)    Push remote image to registry
	@echo   make r-reflow-remove                $(HELP_COLUMN_SEPARATOR)    Remove local copy of remote image
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-remote-reflow-runtime:
	@echo [Remote - Reflow Runtime] $(call HELP_TOTAL,REMOTE_REFLOW_RUNTIME)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make r-reflow-init                  $(HELP_COLUMN_SEPARATOR)    Run initialization from remote image
	@echo   make r-reflow-init-dryrun           $(HELP_COLUMN_SEPARATOR)    Preview initialization
	@echo   make r-reflow-init-all              $(HELP_COLUMN_SEPARATOR)    Initialize all resources
	@echo   make r-reflow-init-config           $(HELP_COLUMN_SEPARATOR)    Initialize configuration files only
	@echo   make r-reflow-init-force            $(HELP_COLUMN_SEPARATOR)    Initialize and overwrite files
	@echo   make r-reflow-init-ask              $(HELP_COLUMN_SEPARATOR)    Initialize with confirmation prompts
	@$(ECHO_BLANK)
	@echo   make r-reflow-releases-recover      $(HELP_COLUMN_SEPARATOR)    Run release recovery
	@echo   make r-reflow-releases-recover-dryrun $(HELP_COLUMN_SEPARATOR)  Preview release recovery
	@echo   make r-reflow-tags-convert          $(HELP_COLUMN_SEPARATOR)    Convert version tags
	@echo   make r-reflow-tags-convert-dryrun   $(HELP_COLUMN_SEPARATOR)    Preview tag conversion
	@echo   make r-reflow-dockerize             $(HELP_COLUMN_SEPARATOR)    Run Docker release automation
	@echo   make r-reflow-dockerize-dryrun      $(HELP_COLUMN_SEPARATOR)    Preview Docker release automation
	@$(ECHO_BLANK)
	@echo   make r-reflow-tags-replay           $(HELP_COLUMN_SEPARATOR)    Deprecated release-recovery alias
	@echo   make r-reflow-tags-replay-dryrun    $(HELP_COLUMN_SEPARATOR)    Deprecated dry-run alias
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
