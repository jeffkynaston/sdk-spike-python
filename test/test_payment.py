"""
    Plastiq Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.payer_id import PayerId
from openapi_client.model.payment_details import PaymentDetails
from openapi_client.model.payment_intent_fees import PaymentIntentFees
from openapi_client.model.payment_method_id import PaymentMethodId
from openapi_client.model.recipient_id import RecipientId
globals()['PayerId'] = PayerId
globals()['PaymentDetails'] = PaymentDetails
globals()['PaymentIntentFees'] = PaymentIntentFees
globals()['PaymentMethodId'] = PaymentMethodId
globals()['RecipientId'] = RecipientId
from openapi_client.model.payment import Payment


class TestPayment(unittest.TestCase):
    """Payment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPayment(self):
        """Test Payment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Payment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
