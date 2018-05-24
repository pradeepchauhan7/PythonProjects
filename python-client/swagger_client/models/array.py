# coding: utf-8

"""
    defaultTitle

    defaultDescription  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Array(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'int',
        'name': 'str',
        'desc': 'str',
        'image': 'str',
        'expiry': 'str',
        'status': 'bool',
        'domain': 'str',
        'attrs': 'str',
        'admin': 'int',
        'template': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'desc': 'desc',
        'image': 'image',
        'expiry': 'expiry',
        'status': 'status',
        'domain': 'domain',
        'attrs': 'attrs',
        'admin': 'admin',
        'template': 'template'
    }

    def __init__(self, id=None, name=None, desc=None, image=None, expiry=None, status=None, domain=None, attrs=None, admin=None, template=None):  # noqa: E501
        """Array - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._desc = None
        self._image = None
        self._expiry = None
        self._status = None
        self._domain = None
        self._attrs = None
        self._admin = None
        self._template = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if image is not None:
            self.image = image
        if expiry is not None:
            self.expiry = expiry
        if status is not None:
            self.status = status
        if domain is not None:
            self.domain = domain
        if attrs is not None:
            self.attrs = attrs
        if admin is not None:
            self.admin = admin
        if template is not None:
            self.template = template

    @property
    def id(self):
        """Gets the id of this Array.  # noqa: E501


        :return: The id of this Array.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Array.


        :param id: The id of this Array.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Array.  # noqa: E501


        :return: The name of this Array.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Array.


        :param name: The name of this Array.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this Array.  # noqa: E501


        :return: The desc of this Array.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this Array.


        :param desc: The desc of this Array.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def image(self):
        """Gets the image of this Array.  # noqa: E501


        :return: The image of this Array.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Array.


        :param image: The image of this Array.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def expiry(self):
        """Gets the expiry of this Array.  # noqa: E501


        :return: The expiry of this Array.  # noqa: E501
        :rtype: str
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this Array.


        :param expiry: The expiry of this Array.  # noqa: E501
        :type: str
        """

        self._expiry = expiry

    @property
    def status(self):
        """Gets the status of this Array.  # noqa: E501


        :return: The status of this Array.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Array.


        :param status: The status of this Array.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def domain(self):
        """Gets the domain of this Array.  # noqa: E501


        :return: The domain of this Array.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Array.


        :param domain: The domain of this Array.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def attrs(self):
        """Gets the attrs of this Array.  # noqa: E501


        :return: The attrs of this Array.  # noqa: E501
        :rtype: str
        """
        return self._attrs

    @attrs.setter
    def attrs(self, attrs):
        """Sets the attrs of this Array.


        :param attrs: The attrs of this Array.  # noqa: E501
        :type: str
        """

        self._attrs = attrs

    @property
    def admin(self):
        """Gets the admin of this Array.  # noqa: E501


        :return: The admin of this Array.  # noqa: E501
        :rtype: int
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this Array.


        :param admin: The admin of this Array.  # noqa: E501
        :type: int
        """

        self._admin = admin

    @property
    def template(self):
        """Gets the template of this Array.  # noqa: E501


        :return: The template of this Array.  # noqa: E501
        :rtype: int
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Array.


        :param template: The template of this Array.  # noqa: E501
        :type: int
        """

        self._template = template

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Array):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other