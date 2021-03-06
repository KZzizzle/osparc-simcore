# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from .base_model_ import Model
from .. import util


class InlineResponseDefaultError(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message: str=None, errors: List[object]=None, status: int=None):
        """InlineResponseDefaultError - a model defined in OpenAPI

        :param message: The message of this InlineResponseDefaultError.
        :param errors: The errors of this InlineResponseDefaultError.
        :param status: The status of this InlineResponseDefaultError.
        """
        self.openapi_types = {
            'message': str,
            'errors': List[object],
            'status': int
        }

        self.attribute_map = {
            'message': 'message',
            'errors': 'errors',
            'status': 'status'
        }

        self._message = message
        self._errors = errors
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InlineResponseDefaultError':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inline_response_default_error of this InlineResponseDefaultError.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self):
        """Gets the message of this InlineResponseDefaultError.

        Error message

        :return: The message of this InlineResponseDefaultError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponseDefaultError.

        Error message

        :param message: The message of this InlineResponseDefaultError.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def errors(self):
        """Gets the errors of this InlineResponseDefaultError.


        :return: The errors of this InlineResponseDefaultError.
        :rtype: List[object]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InlineResponseDefaultError.


        :param errors: The errors of this InlineResponseDefaultError.
        :type errors: List[object]
        """

        self._errors = errors

    @property
    def status(self):
        """Gets the status of this InlineResponseDefaultError.

        Error code

        :return: The status of this InlineResponseDefaultError.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponseDefaultError.

        Error code

        :param status: The status of this InlineResponseDefaultError.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status
