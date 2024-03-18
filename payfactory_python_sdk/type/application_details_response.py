# coding: utf-8

"""
    Payfactory Api

    Payfactory specializes in embedded payment facilitation (payfac) services for ISVs and SaaS companies. Our gateway-friendly platform integrates with software systems to provide seamless payment facilitation with little to no development required, allowing our partners to minimize integration costs and quickly gain a new revenue stream. Founded by payment industry veterans, we believe that integrated processing should be simple, frictionless and fast – while also maintaining the highest level of security, customer service and human support.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from payfactory_python_sdk.type.address_model import AddressModel
from payfactory_python_sdk.type.application_details_response_customer_service_model import ApplicationDetailsResponseCustomerServiceModel
from payfactory_python_sdk.type.application_details_response_signer_model import ApplicationDetailsResponseSignerModel

class RequiredApplicationDetailsResponse(TypedDict):
    pass

class OptionalApplicationDetailsResponse(TypedDict, total=False):
    appId: typing.Optional[str]

    externalId: typing.Optional[str]

    legalName: typing.Optional[str]

    dbaName: typing.Optional[str]

    ownershipType: typing.Optional[str]

    taxId: typing.Optional[str]

    address: AddressModel

    phone: typing.Optional[str]

    website: typing.Optional[str]

    customerService: ApplicationDetailsResponseCustomerServiceModel

    signer: ApplicationDetailsResponseSignerModel

    monthlyTransactionVolume: int

    merchantCategoryCode: typing.Optional[str]

class ApplicationDetailsResponse(RequiredApplicationDetailsResponse, OptionalApplicationDetailsResponse):
    pass