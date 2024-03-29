# coding: utf-8

"""
    Payfactory Api

    Payfactory specializes in embedded payment facilitation (payfac) services for ISVs and SaaS companies. Our gateway-friendly platform integrates with software systems to provide seamless payment facilitation with little to no development required, allowing our partners to minimize integration costs and quickly gain a new revenue stream. Founded by payment industry veterans, we believe that integrated processing should be simple, frictionless and fast – while also maintaining the highest level of security, customer service and human support.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from payfactory_python_sdk import schemas  # noqa: F401


class CardTypeEnum(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "UNKNOWN": "UNKNOWN",
            "Visa": "VISA",
            "MasterCard": "MASTER_CARD",
            "AmericanExpress": "AMERICAN_EXPRESS",
            "Discover": "DISCOVER",
        }
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("UNKNOWN")
    
    @schemas.classproperty
    def VISA(cls):
        return cls("Visa")
    
    @schemas.classproperty
    def MASTER_CARD(cls):
        return cls("MasterCard")
    
    @schemas.classproperty
    def AMERICAN_EXPRESS(cls):
        return cls("AmericanExpress")
    
    @schemas.classproperty
    def DISCOVER(cls):
        return cls("Discover")
