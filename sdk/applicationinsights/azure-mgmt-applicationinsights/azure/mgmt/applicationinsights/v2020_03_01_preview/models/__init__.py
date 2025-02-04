# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ComponentLinkedStorageAccounts
    from ._models_py3 import ComponentLinkedStorageAccountsPatch
    from ._models_py3 import ErrorResponseLinkedStorage
    from ._models_py3 import ErrorResponseLinkedStorageError
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
except (SyntaxError, ImportError):
    from ._models import ComponentLinkedStorageAccounts  # type: ignore
    from ._models import ComponentLinkedStorageAccountsPatch  # type: ignore
    from ._models import ErrorResponseLinkedStorage  # type: ignore
    from ._models import ErrorResponseLinkedStorageError  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore

from ._application_insights_management_client_enums import (
    StorageType,
)

__all__ = [
    'ComponentLinkedStorageAccounts',
    'ComponentLinkedStorageAccountsPatch',
    'ErrorResponseLinkedStorage',
    'ErrorResponseLinkedStorageError',
    'ProxyResource',
    'Resource',
    'StorageType',
]
