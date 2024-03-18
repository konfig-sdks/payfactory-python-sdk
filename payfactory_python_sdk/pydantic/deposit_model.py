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

from payfactory_python_sdk.pydantic.deposit_type import DepositType
from payfactory_python_sdk.pydantic.transaction_model import TransactionModel

class DepositModel(BaseModel):
    date: typing.Optional[datetime] = Field(None, alias='date')

    type: typing.Optional[DepositType] = Field(None, alias='type')

    sub_merchant_id: typing.Optional[typing.Optional[str]] = Field(None, alias='subMerchantId')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    transactions: typing.Optional[typing.Optional[typing.List[TransactionModel]]] = Field(None, alias='transactions')
    class Config:
        arbitrary_types_allowed = True
