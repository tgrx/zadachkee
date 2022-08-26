define log
	@tput bold 2>/dev/null || exit 0
	@tput setab 0  2>/dev/null || exit 0
	@tput setaf 4  2>/dev/null || exit 0
	@echo -n '-*-    $(1)    -*-'
	@tput sgr0  2>/dev/null || exit 0
	@echo ""
	@tput sgr0  2>/dev/null || exit 0
endef


DIR_ARTIFACTS := $(abspath $(DIR_REPO)/.artifacts)
DIR_PYTHON_VENV := $(shell poetry env info --path 2>/dev/null)
DIR_REPO := $(realpath ./)
