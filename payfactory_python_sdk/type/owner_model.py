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

class RequiredOwnerModel(TypedDict):
    title: str

    firstName: str

    lastName: str

    email: str

    phone: str

    ownershipPercentage: int

class OptionalOwnerModel(TypedDict, total=False):
    # Date of birth
    dob: typing.Optional[datetime]

    # Social Security Number
    ssn: typing.Optional[str]

    homeAddress: AddressModel

class OwnerModel(RequiredOwnerModel, OptionalOwnerModel):
    pass
