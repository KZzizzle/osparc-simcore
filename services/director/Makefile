#
# Targets for DEVELOPMENT for Director service
#
include ../../scripts/common.Makefile
include ../../scripts/common-service.Makefile


.PHONY: openapi-specs
openapi-specs: ## updates and validates openapi specifications
	$(MAKE) -C $(CURDIR)/src/simcore_service_${APP_NAME}/api $@
