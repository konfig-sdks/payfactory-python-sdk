# coding: utf-8
"""
    Payfactory Api

    Payfactory specializes in embedded payment facilitation (payfac) services for ISVs and SaaS companies. Our gateway-friendly platform integrates with software systems to provide seamless payment facilitation with little to no development required, allowing our partners to minimize integration costs and quickly gain a new revenue stream. Founded by payment industry veterans, we believe that integrated processing should be simple, frictionless and fast – while also maintaining the highest level of security, customer service and human support.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from payfactory_python_sdk.client_custom import ClientCustom
from payfactory_python_sdk.configuration import Configuration
from payfactory_python_sdk.api_client import ApiClient
from payfactory_python_sdk.type_util import copy_signature
from payfactory_python_sdk.apis.tags.application_api import ApplicationApi
from payfactory_python_sdk.apis.tags.application_form_api import ApplicationFormApi
from payfactory_python_sdk.apis.tags.document_api import DocumentApi
from payfactory_python_sdk.apis.tags.reporting_api import ReportingApi
from payfactory_python_sdk.apis.tags.transaction_api import TransactionApi



class Payfactory(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.application: ApplicationApi = ApplicationApi(api_client)
        self.application_form: ApplicationFormApi = ApplicationFormApi(api_client)
        self.document: DocumentApi = DocumentApi(api_client)
        self.reporting: ReportingApi = ReportingApi(api_client)
        self.transaction: TransactionApi = TransactionApi(api_client)