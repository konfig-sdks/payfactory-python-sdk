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
from pydantic import BaseModel, Field, RootModel

from payfactory_python_sdk.pydantic.address_model import AddressModel
from payfactory_python_sdk.pydantic.application_details_response_customer_service_model import ApplicationDetailsResponseCustomerServiceModel
from payfactory_python_sdk.pydantic.application_details_response_signer_model import ApplicationDetailsResponseSignerModel

class ApplicationDetailsResponse(BaseModel):
    app_id: typing.Optional[typing.Optional[str]] = Field(None, alias='appId')

    external_id: typing.Optional[typing.Optional[str]] = Field(None, alias='externalId')

    legal_name: typing.Optional[typing.Optional[str]] = Field(None, alias='legalName')

    dba_name: typing.Optional[typing.Optional[str]] = Field(None, alias='dbaName')

    ownership_type: typing.Optional[typing.Optional[str]] = Field(None, alias='ownershipType')

    tax_id: typing.Optional[typing.Optional[str]] = Field(None, alias='taxId')

    address: typing.Optional[AddressModel] = Field(None, alias='address')

    phone: typing.Optional[typing.Optional[str]] = Field(None, alias='phone')

    website: typing.Optional[typing.Optional[str]] = Field(None, alias='website')

    customer_service: typing.Optional[ApplicationDetailsResponseCustomerServiceModel] = Field(None, alias='customerService')

    signer: typing.Optional[ApplicationDetailsResponseSignerModel] = Field(None, alias='signer')

    monthly_transaction_volume: typing.Optional[int] = Field(None, alias='monthlyTransactionVolume')

    merchant_category_code: typing.Optional[typing.Optional[str]] = Field(None, alias='merchantCategoryCode')
    class Config:
        arbitrary_types_allowed = True
