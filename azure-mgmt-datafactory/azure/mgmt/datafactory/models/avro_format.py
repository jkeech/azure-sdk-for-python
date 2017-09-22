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

from .dataset_storage_format import DatasetStorageFormat


class AvroFormat(DatasetStorageFormat):
    """The data stored in Avro format.

    :param serializer: Serializer. Type: string (or Expression with resultType
     string).
    :type serializer: object
    :param deserializer: Deserializer. Type: string (or Expression with
     resultType string).
    :type deserializer: object
    :param type: Polymorphic Discriminator
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    def __init__(self, serializer=None, deserializer=None):
        super(AvroFormat, self).__init__(serializer=serializer, deserializer=deserializer)
        self.type = 'AvroFormat'
