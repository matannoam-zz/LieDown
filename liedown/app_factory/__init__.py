from flask import Flask

from .. import config

from .register_blueprints import register_blueprints
from .initialize_extensions import initialize_extensions
from .configure_logging import configure_logging


def create_app(package_name, package_path, settings_override=None,
               extensions=None):
    """Returns a :class:`Flask` application instance configured with common
    functionality for this application.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param extensions: an array of instances of additional extensions to
        initialize on the app
    """

    app = Flask(package_name)
    app.config.from_object(config.Common())
    app.config.from_object(settings_override)

    register_blueprints(app, package_name, package_path)

    common_extensions = frozenset([])
    initialize_extensions(app, common_extensions)
    initialize_extensions(app, extensions)
    configure_logging(app)

    return app
