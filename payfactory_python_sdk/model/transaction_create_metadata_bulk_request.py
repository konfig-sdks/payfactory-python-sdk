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


class TransactionCreateMetadataBulkRequest(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TransactionMetadataRequest']:
            return TransactionMetadataRequest

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TransactionMetadataRequest'], typing.List['TransactionMetadataRequest']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TransactionCreateMetadataBulkRequest':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TransactionMetadataRequest':
        return super().__getitem__(i)

from payfactory_python_sdk.model.transaction_metadata_request import TransactionMetadataRequest
