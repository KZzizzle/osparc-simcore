# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .simcore_node import SimcoreNode  # noqa: F401,E501
from .. import util


class InlineResponse2001(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[SimcoreNode]=None, error: object=None):  # noqa: E501
        """InlineResponse2001 - a model defined in OpenAPI

        :param data: The data of this InlineResponse2001.  # noqa: E501
        :type data: List[SimcoreNode]
        :param error: The error of this InlineResponse2001.  # noqa: E501
        :type error: object
        """
        self.openapi_types = {
            'data': List[SimcoreNode],
            'error': object
        }

        self.attribute_map = {
            'data': 'data',
            'error': 'error'
        }

        self._data = data
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[SimcoreNode]:
        """Gets the data of this InlineResponse2001.


        :return: The data of this InlineResponse2001.
        :rtype: List[SimcoreNode]
        """
        return self._data

    @data.setter
    def data(self, data: List[SimcoreNode]):
        """Sets the data of this InlineResponse2001.


        :param data: The data of this InlineResponse2001.
        :type data: List[SimcoreNode]
        """

        self._data = data

    @property
    def error(self) -> object:
        """Gets the error of this InlineResponse2001.


        :return: The error of this InlineResponse2001.
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error: object):
        """Sets the error of this InlineResponse2001.


        :param error: The error of this InlineResponse2001.
        :type error: object
        """

        self._error = error
