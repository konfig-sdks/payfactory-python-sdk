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


class TransactionModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            date = schemas.DateTimeSchema
            amount = schemas.Float64Schema
            fee = schemas.Float64Schema
            
            
            class maskedPan(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'maskedPan':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def cardType() -> typing.Type['CardTypeEnum']:
                return CardTypeEnum
            
            
            class cardholderName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cardholderName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class expDate(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class type(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'type':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class refNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'refNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class batchId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'batchId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class authCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'authCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class userData(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'userData':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "date": date,
                "amount": amount,
                "fee": fee,
                "maskedPan": maskedPan,
                "cardType": cardType,
                "cardholderName": cardholderName,
                "expDate": expDate,
                "type": type,
                "refNumber": refNumber,
                "batchId": batchId,
                "authCode": authCode,
                "userData": userData,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fee"]) -> MetaOapg.properties.fee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maskedPan"]) -> MetaOapg.properties.maskedPan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardType"]) -> 'CardTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardholderName"]) -> MetaOapg.properties.cardholderName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expDate"]) -> MetaOapg.properties.expDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refNumber"]) -> MetaOapg.properties.refNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batchId"]) -> MetaOapg.properties.batchId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authCode"]) -> MetaOapg.properties.authCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userData"]) -> MetaOapg.properties.userData: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "amount", "fee", "maskedPan", "cardType", "cardholderName", "expDate", "type", "refNumber", "batchId", "authCode", "userData", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fee"]) -> typing.Union[MetaOapg.properties.fee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maskedPan"]) -> typing.Union[MetaOapg.properties.maskedPan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardType"]) -> typing.Union['CardTypeEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardholderName"]) -> typing.Union[MetaOapg.properties.cardholderName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expDate"]) -> typing.Union[MetaOapg.properties.expDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refNumber"]) -> typing.Union[MetaOapg.properties.refNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batchId"]) -> typing.Union[MetaOapg.properties.batchId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authCode"]) -> typing.Union[MetaOapg.properties.authCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userData"]) -> typing.Union[MetaOapg.properties.userData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "amount", "fee", "maskedPan", "cardType", "cardholderName", "expDate", "type", "refNumber", "batchId", "authCode", "userData", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, datetime, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        fee: typing.Union[MetaOapg.properties.fee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maskedPan: typing.Union[MetaOapg.properties.maskedPan, None, str, schemas.Unset] = schemas.unset,
        cardType: typing.Union['CardTypeEnum', schemas.Unset] = schemas.unset,
        cardholderName: typing.Union[MetaOapg.properties.cardholderName, None, str, schemas.Unset] = schemas.unset,
        expDate: typing.Union[MetaOapg.properties.expDate, None, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, None, str, schemas.Unset] = schemas.unset,
        refNumber: typing.Union[MetaOapg.properties.refNumber, None, str, schemas.Unset] = schemas.unset,
        batchId: typing.Union[MetaOapg.properties.batchId, None, str, schemas.Unset] = schemas.unset,
        authCode: typing.Union[MetaOapg.properties.authCode, None, str, schemas.Unset] = schemas.unset,
        userData: typing.Union[MetaOapg.properties.userData, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionModel':
        return super().__new__(
            cls,
            *args,
            date=date,
            amount=amount,
            fee=fee,
            maskedPan=maskedPan,
            cardType=cardType,
            cardholderName=cardholderName,
            expDate=expDate,
            type=type,
            refNumber=refNumber,
            batchId=batchId,
            authCode=authCode,
            userData=userData,
            _configuration=_configuration,
            **kwargs,
        )

from payfactory_python_sdk.model.card_type_enum import CardTypeEnum
