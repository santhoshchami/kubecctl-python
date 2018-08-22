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


class V1VolumeProjection(object):
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
        'config_map': 'V1ConfigMapProjection',
        'downward_api': 'V1DownwardAPIProjection',
        'secret': 'V1SecretProjection'
    }

    attribute_map = {
        'config_map': 'configMap',
        'downward_api': 'downwardAPI',
        'secret': 'secret'
    }

    def __init__(self, config_map=None, downward_api=None, secret=None):
        """
        V1VolumeProjection - a model defined in Swagger
        """

        self._config_map = None
        self._downward_api = None
        self._secret = None
        self.discriminator = None

        if config_map is not None:
          self.config_map = config_map
        if downward_api is not None:
          self.downward_api = downward_api
        if secret is not None:
          self.secret = secret

    @property
    def config_map(self):
        """
        Gets the config_map of this V1VolumeProjection.
        information about the configMap data to project

        :return: The config_map of this V1VolumeProjection.
        :rtype: V1ConfigMapProjection
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """
        Sets the config_map of this V1VolumeProjection.
        information about the configMap data to project

        :param config_map: The config_map of this V1VolumeProjection.
        :type: V1ConfigMapProjection
        """

        self._config_map = config_map

    @property
    def downward_api(self):
        """
        Gets the downward_api of this V1VolumeProjection.
        information about the downwardAPI data to project

        :return: The downward_api of this V1VolumeProjection.
        :rtype: V1DownwardAPIProjection
        """
        return self._downward_api

    @downward_api.setter
    def downward_api(self, downward_api):
        """
        Sets the downward_api of this V1VolumeProjection.
        information about the downwardAPI data to project

        :param downward_api: The downward_api of this V1VolumeProjection.
        :type: V1DownwardAPIProjection
        """

        self._downward_api = downward_api

    @property
    def secret(self):
        """
        Gets the secret of this V1VolumeProjection.
        information about the secret data to project

        :return: The secret of this V1VolumeProjection.
        :rtype: V1SecretProjection
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this V1VolumeProjection.
        information about the secret data to project

        :param secret: The secret of this V1VolumeProjection.
        :type: V1SecretProjection
        """

        self._secret = secret

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
        if not isinstance(other, V1VolumeProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other