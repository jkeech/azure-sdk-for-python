# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IntegrationRuntimeRegenerateKeyParameters(Model):
    """Parameters to regenerate the authentication key.

    :param key_name: The name of the authentication key to regenerate.
     Possible values include: 'authKey1', 'authKey2'
    :type key_name: str or :class:`IntegrationRuntimeAuthKeyName
     <azure.mgmt.datafactory.models.IntegrationRuntimeAuthKeyName>`
    """

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
    }

    def __init__(self, key_name=None):
        self.key_name = key_name
