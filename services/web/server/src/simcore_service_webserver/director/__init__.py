""" director subsystem

    Provides access to the director backend service
"""

import logging

from aiohttp import ClientSession, web
from servicelib.application_keys import APP_CONFIG_KEY
from servicelib.rest_routing import (get_handlers_from_namespace,
                                     iter_path_operations,
                                     map_handlers_with_operations)
from yarl import URL

from ..rest_config import APP_OPENAPI_SPECS_KEY
from . import handlers
from .config import APP_DIRECTOR_API_KEY, CONFIG_SECTION_NAME, build_api_url
from .registry import InteractiveServiceLocalRegistry, set_registry

logger = logging.getLogger(__name__)




def setup(app: web.Application,* , disable_login=False):
    """ Sets up director's subsystem

    :param app: main application
    :type app: web.Application
    :param disable_login: disabled auth requirements for subsystem's rest (for debugging), defaults to False
    :param disable_login: bool, optional
    """
    logger.debug("Setting up %s ...", __name__)

    cfg = app[APP_CONFIG_KEY][CONFIG_SECTION_NAME]

    if not cfg["enabled"]:
        logger.warning("'%s' explicitly disabled in config", __name__)
        return

    # director service API base url, e.g. http://director:8081/v0
    app[APP_DIRECTOR_API_KEY] = build_api_url(cfg)

    set_registry(app, InteractiveServiceLocalRegistry())

    # setup routes ------------
    specs = app[APP_OPENAPI_SPECS_KEY]

    def include_path(tup_object):
        _method, path, _operation_id = tup_object
        return any( tail in path  for tail in ['/running_interactive_services', '/services'] )

    handlers_dict = {
        'running_interactive_services_post': handlers.running_interactive_services_post ,
        'running_interactive_services_get': handlers.running_interactive_services_get,
        'running_interactive_services_delete': handlers.running_interactive_services_delete,
        'running_interactive_services_delete_all': handlers.running_interactive_services_delete_all,
        'services_get': handlers.services_get
    }

    # Disables login_required decorator for testing purposes
    if disable_login:
        for name, hnds in handlers_dict.items():
            if hasattr(hnds, '__wrapped__'):
                handlers_dict[name] = hnds.__wrapped__

    routes = map_handlers_with_operations(
        handlers_dict,
        filter(include_path, iter_path_operations(specs)),
        strict=True
    )
    app.router.add_routes(routes)


# alias
setup_director = setup

__all__ = (
    'setup_director'
)
