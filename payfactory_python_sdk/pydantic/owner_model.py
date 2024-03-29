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

class OwnerModel(BaseModel):
    title: str = Field(alias='title')

    first_name: str = Field(alias='firstName')

    last_name: str = Field(alias='lastName')

    email: str = Field(alias='email')

    phone: str = Field(alias='phone')

    ownership_percentage: int = Field(alias='ownershipPercentage')

    # Date of birth
    dob: typing.Optional[typing.Optional[datetime]] = Field(None, alias='dob')

    # Social Security Number
    ssn: typing.Optional[typing.Optional[str]] = Field(None, alias='ssn')

    home_address: typing.Optional[AddressModel] = Field(None, alias='homeAddress')
    class Config:
        arbitrary_types_allowed = True
