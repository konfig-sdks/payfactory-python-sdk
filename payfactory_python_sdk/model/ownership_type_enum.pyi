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


class OwnershipTypeEnum(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("Unknown")
    
    @schemas.classproperty
    def SOLE_PROPRIETORSHIP(cls):
        return cls("SoleProprietorship")
    
    @schemas.classproperty
    def PARTNERSHIP(cls):
        return cls("Partnership")
    
    @schemas.classproperty
    def PRIVATE_CORPORATION(cls):
        return cls("PrivateCorporation")
    
    @schemas.classproperty
    def FINANCIAL_INSTITUTION(cls):
        return cls("FinancialInstitution")
    
    @schemas.classproperty
    def NON_PROFIT(cls):
        return cls("NonProfit")
    
    @schemas.classproperty
    def GOVERNMENT(cls):
        return cls("Government")
    
    @schemas.classproperty
    def PUBLIC_CORPORATION(cls):
        return cls("PublicCorporation")
    
    @schemas.classproperty
    def SECREGULATED_CORPORATION(cls):
        return cls("SECRegulatedCorporation")
    
    @schemas.classproperty
    def TRUST(cls):
        return cls("Trust")
    
    @schemas.classproperty
    def LIMITED_LIABILITY_COMPANY(cls):
        return cls("LimitedLiabilityCompany")
