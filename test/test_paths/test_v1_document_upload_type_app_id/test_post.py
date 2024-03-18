# coding: utf-8

"""
    Payfactory Api

    Payfactory specializes in embedded payment facilitation (payfac) services for ISVs and SaaS companies. Our gateway-friendly platform integrates with software systems to provide seamless payment facilitation with little to no development required, allowing our partners to minimize integration costs and quickly gain a new revenue stream. Founded by payment industry veterans, we believe that integrated processing should be simple, frictionless and fast – while also maintaining the highest level of security, customer service and human support.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import payfactory_python_sdk
from payfactory_python_sdk.paths.v1_document_upload_type_app_id import post
from payfactory_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1DocumentUploadTypeAppId(ApiTestMixin, unittest.TestCase):
    """
    V1DocumentUploadTypeAppId unit test stubs
        Upload an Agreement for a new Application
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
