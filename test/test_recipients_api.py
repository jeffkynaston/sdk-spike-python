"""
    Plastiq Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.recipients_api import RecipientsApi  # noqa: E501


class TestRecipientsApi(unittest.TestCase):
    """RecipientsApi unit test stubs"""

    def setUp(self):
        self.api = RecipientsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_recipients_get(self):
        """Test case for recipients_get

        Retrieve a paginated list of Recipients by query parameter(s)  # noqa: E501
        """
        pass

    def test_recipients_id_delete(self):
        """Test case for recipients_id_delete

        Delete a Recipient  # noqa: E501
        """
        pass

    def test_recipients_id_get(self):
        """Test case for recipients_id_get

        Retrieve a Recipient  # noqa: E501
        """
        pass

    def test_recipients_id_patch(self):
        """Test case for recipients_id_patch

        Update a Recipient  # noqa: E501
        """
        pass

    def test_recipients_post(self):
        """Test case for recipients_post

        Create a Recipient  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
