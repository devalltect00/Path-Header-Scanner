# Read-only Git inspection helpers.

GIT_COMMANDS_LIST := git-current-branch git-url-origin git-log git-tags
$(foreach cmd,$(GIT_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,GIT,$(cmd),LOCAL)))

.PHONY: git-current-branch git-url-origin git-log git-tags
git-current-branch:
	git branch --show-current

git-url-origin:
	git remote get-url origin

git-log:
	git log --oneline --graph --decorate --all -n 25

git-tags:
	git log --no-walk --tags --pretty="format:%h %d %s"
