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


class AzureKeyVaultReference(Model):
    """A reference to an object in Azure Key Vault.

    :param store: The Azure Key Vault LinkedService.
    :type store: :class:`LinkedServiceReference
     <azure.mgmt.datafactory.models.LinkedServiceReference>`
    :param type: Polymorphic Discriminator
    :type type: str
    """

    _validation = {
        'store': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'store': {'key': 'store', 'type': 'LinkedServiceReference'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'AzureKeyVaultSecret': 'AzureKeyVaultSecretReference'}
    }

    def __init__(self, store):
        self.store = store
        self.type = None
