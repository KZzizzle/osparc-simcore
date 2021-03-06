#
# Targets for DEVELOPMENT of Public API Server
#
include ../../scripts/common.Makefile
include ../../scripts/common-service.Makefile


.PHONY: reqs
reqs: ## compiles pip requirements (.in -> .txt)
	@$(MAKE_C) requirements reqs




# DEVELOPMENT TOOLS ########

.env:
	cp .env-devel $@

docker-compose.yml:
	cp $(CURDIR)/tests/utils/docker-compose.yml $@

.PHONY: run-devel down
run-devel: .env docker-compose.yml down ## runs app on host with pg fixture for development [for development]
	# Starting db (under $<)
	docker-compose up --detach
	# Creating db-tables: user=key, password=secret
	@$(MAKE) db-tables
	# start app (under $<)
	uvicorn simcore_service_api_server.__main__:the_app \
		--reload --reload-dir $(SRC_DIR) \
		--port=8000 --host=0.0.0.0

.PHONY: db-tables
db-tables: .env ## upgrades and create tables [for development]
	# Upgrading and creating tables
	export $(shell grep -v '^#' $< | xargs  -d '\n'); \
	python3 tests/utils/init-pg.py

.PHONY: db-migration
db-migration: .env ## runs discover and upgrade on running pg-db [for development]
	# Creating tables
	export $(shell grep -v '^#' $< | xargs  -d '\n'); \
	sc-pg discover && sc-pg upgrade

down: docker-compose.yml ## stops pg fixture
	# stopping extra services
	-@docker-compose -f $< down
	# killing any process using port 8000
	-@fuser --kill --verbose --namespace tcp 8000



# BUILD ########

.PHONY: openapi-specs openapi.json
openapi-specs: openapi.json
openapi.json: .env
	# generating openapi specs file
	python3 -c "import json; from $(APP_PACKAGE_NAME).__main__ import *; print( json.dumps(the_app.openapi(), indent=2) )" > $@


# GENERATION python client ########
.PHONY: python-client generator-help

# SEE https://openapi-generator.tech/docs/usage#generate
# SEE https://openapi-generator.tech/docs/generators/python
#
# TODO: put instead to additional-props.yaml and --config=openapi-generator/python-config.yaml
# TODO: copy this code to https://github.com/ITISFoundation/osparc-simcore-python-client/blob/master/Makefile
#

# NOTE: assumes this repo exists
GIT_USER_ID := ITISFoundation
GIT_REPO_ID := osparc-simcore-python-client

SCRIPTS_DIR := $(abspath $(CURDIR)/../../scripts)
GENERATOR_NAME := python

ADDITIONAL_PROPS := \
	generateSourceCodeOnly=false\
	hideGenerationTimestamp=true\
	library=urllib3\
	packageName=osparc\
	packageUrl=https://github.com/$(GIT_USER_ID)/${GIT_REPO_ID}.git\
	packageVersion=$(APP_VERSION)\
	projectName=osparc-simcore-python-api
ADDITIONAL_PROPS := $(foreach prop,$(ADDITIONAL_PROPS),$(strip $(prop)))

null  :=
space := $(null) #
comma := ,

client:
	# cloning $(GIT_USER_ID)/$(GIT_REPO_ID) -> $@
	git clone git@github.com:$(GIT_USER_ID)/$(GIT_REPO_ID).git $@
	cd client; git checkout -b "upgrade-${APP_VERSION}"


python-client: client openapi.json ## runs python client generator
	cd $(CURDIR); \
	$(SCRIPTS_DIR)/openapi-generator-cli.bash generate \
		--generator-name=$(GENERATOR_NAME) \
		--git-user-id=$(GIT_USER_ID)\
		--git-repo-id=$(GIT_REPO_ID)\
		--http-user-agent="osparc-api/{packageVersion}/{language}"\
		--input-spec=/local/openapi.json \
		--output=/local/client \
		--additional-properties=$(subst $(space),$(comma),$(strip $(ADDITIONAL_PROPS)))\
		--package-name=osparc\
		--release-note="Updated to $(APP_VERSION)"


generator-help: ## help on client-api generator
	# generate help
	@$(SCRIPTS_DIR)/openapi-generator-cli.bash help generate
	# generator config help
	@$(SCRIPTS_DIR)/openapi-generator-cli.bash config-help -g $(GENERATOR_NAME)
