# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import os
import json
import logging
from msal_extensions.osx import Keychain, KeychainError
from .._constants import VSCODE_CREDENTIALS_SECTION

_LOGGER = logging.getLogger(__name__)


def get_user_settings():
    try:
        path = os.path.join(os.environ["HOME"], "Library", "Application Support", "Code", "User", "settings.json")
        with open(path) as file:
            return json.load(file)
    except Exception as ex:  # pylint:disable=broad-except
        _LOGGER.debug('Exception reading VS Code user settings: "%s"', ex, exc_info=_LOGGER.isEnabledFor(logging.DEBUG))
        return {}


def get_refresh_token(cloud_name):
    try:
        key_chain = Keychain()
        return key_chain.get_generic_password(VSCODE_CREDENTIALS_SECTION, cloud_name)
    except KeychainError:
        return None
    except Exception as ex:  # pylint:disable=broad-except
        _LOGGER.debug(
            'Exception retrieving VS Code credentials: "%s"', ex, exc_info=_LOGGER.isEnabledFor(logging.DEBUG)
        )
        return None
