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


class IntegrationRuntimeStatus(Model):
    """Integration runtime status.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar state: The state of integration runtime. Possible values include:
     'Initial', 'Stopped', 'Started', 'Starting', 'Stopping',
     'NeedRegistration', 'Online', 'Limited', 'Offline'
    :vartype state: str or :class:`IntegrationRuntimeState
     <azure.mgmt.datafactory.models.IntegrationRuntimeState>`
    :param type: Polymorphic Discriminator
    :type type: str
    """

    _validation = {
        'state': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'SelfHosted': 'SelfHostedIntegrationRuntimeStatus', 'Managed': 'ManagedIntegrationRuntimeStatus'}
    }

    def __init__(self):
        self.state = None
        self.type = None
