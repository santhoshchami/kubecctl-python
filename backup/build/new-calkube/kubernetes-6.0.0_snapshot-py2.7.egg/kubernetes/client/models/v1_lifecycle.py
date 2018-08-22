# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1Lifecycle(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'post_start': 'V1Handler',
        'pre_stop': 'V1Handler'
    }

    attribute_map = {
        'post_start': 'postStart',
        'pre_stop': 'preStop'
    }

    def __init__(self, post_start=None, pre_stop=None):
        """
        V1Lifecycle - a model defined in Swagger
        """

        self._post_start = None
        self._pre_stop = None
        self.discriminator = None

        if post_start is not None:
          self.post_start = post_start
        if pre_stop is not None:
          self.pre_stop = pre_stop

    @property
    def post_start(self):
        """
        Gets the post_start of this V1Lifecycle.
        PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks

        :return: The post_start of this V1Lifecycle.
        :rtype: V1Handler
        """
        return self._post_start

    @post_start.setter
    def post_start(self, post_start):
        """
        Sets the post_start of this V1Lifecycle.
        PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks

        :param post_start: The post_start of this V1Lifecycle.
        :type: V1Handler
        """

        self._post_start = post_start

    @property
    def pre_stop(self):
        """
        Gets the pre_stop of this V1Lifecycle.
        PreStop is called immediately before a container is terminated. The container is terminated after the handler completes. The reason for termination is passed to the handler. Regardless of the outcome of the handler, the container is eventually terminated. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks

        :return: The pre_stop of this V1Lifecycle.
        :rtype: V1Handler
        """
        return self._pre_stop

    @pre_stop.setter
    def pre_stop(self, pre_stop):
        """
        Sets the pre_stop of this V1Lifecycle.
        PreStop is called immediately before a container is terminated. The container is terminated after the handler completes. The reason for termination is passed to the handler. Regardless of the outcome of the handler, the container is eventually terminated. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks

        :param pre_stop: The pre_stop of this V1Lifecycle.
        :type: V1Handler
        """

        self._pre_stop = pre_stop

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1Lifecycle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
