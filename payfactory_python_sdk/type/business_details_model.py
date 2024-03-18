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
from payfactory_python_sdk.type.ownership_type_enum import OwnershipTypeEnum

class RequiredBusinessDetailsModel(TypedDict):
    address: AddressModel

    phone: str

    # Date your business was established
    establishedDate: date

    # Legal name of your business
    legalName: str

    # The name you are doing business as
    dbaName: str

    # Federal Tax Id
    taxId: str

    # Company website
    website: str

    # Merchant Category Code
    mcc: int

    ownershipType: OwnershipTypeEnum

class OptionalBusinessDetailsModel(TypedDict, total=False):
    pass

class BusinessDetailsModel(RequiredBusinessDetailsModel, OptionalBusinessDetailsModel):
    pass
