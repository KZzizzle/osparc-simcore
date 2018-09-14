# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .running_service import RunningService  # noqa: F401,E501
from .. import util


class RunningServiceEnveloped(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: RunningService=None, status: int=None):  # noqa: E501
        """RunningServiceEnveloped - a model defined in OpenAPI

        :param data: The data of this RunningServiceEnveloped.  # noqa: E501
        :type data: RunningService
        :param status: The status of this RunningServiceEnveloped.  # noqa: E501
        :type status: int
        """
        self.openapi_types = {
            'data': RunningService,
            'status': int
        }

        self.attribute_map = {
            'data': 'data',
            'status': 'status'
        }

        self._data = data
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'RunningServiceEnveloped':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RunningServiceEnveloped of this RunningServiceEnveloped.  # noqa: E501
        :rtype: RunningServiceEnveloped
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> RunningService:
        """Gets the data of this RunningServiceEnveloped.


        :return: The data of this RunningServiceEnveloped.
        :rtype: RunningService
        """
        return self._data

    @data.setter
    def data(self, data: RunningService):
        """Sets the data of this RunningServiceEnveloped.


        :param data: The data of this RunningServiceEnveloped.
        :type data: RunningService
        """

        self._data = data

    @property
    def status(self) -> int:
        """Gets the status of this RunningServiceEnveloped.


        :return: The status of this RunningServiceEnveloped.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this RunningServiceEnveloped.


        :param status: The status of this RunningServiceEnveloped.
        :type status: int
        """

        self._status = status