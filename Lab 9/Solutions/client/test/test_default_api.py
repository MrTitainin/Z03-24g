"""
    Cool product name

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_logged_get(self):
        """Test case for logged_get

        Endpoint for getting active users  # noqa: E501
        """
        pass

    def test_login_get(self):
        """Test case for login_get

        Endpoint for logging users  # noqa: E501
        """
        pass

    def test_receive_get(self):
        """Test case for receive_get

        Endpoint for receiving messages  # noqa: E501
        """
        pass

    def test_register_post(self):
        """Test case for register_post

        Endpoint for registering users  # noqa: E501
        """
        pass

    def test_send_post(self):
        """Test case for send_post

        Endpoint for sending messages  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
