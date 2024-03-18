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


class BusinessDetailsModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "legalName",
            "ownershipType",
            "website",
            "address",
            "establishedDate",
            "phone",
            "taxId",
            "dbaName",
            "mcc",
        }
        
        class properties:
        
            @staticmethod
            def address() -> typing.Type['AddressModel']:
                return AddressModel
            
            
            class phone(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 10
                    min_length = 1
                    regex=[{
                        'pattern': r'^[2-9]\d{9}$',
                    }]
            establishedDate = schemas.DateSchema
            
            
            class legalName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 40
                    min_length = 3
                    regex=[{
                        'pattern': r'^[0-9A-Za-z ,'.&;_\-]+$',
                    }]
            
            
            class dbaName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 40
                    min_length = 3
                    regex=[{
                        'pattern': r'^[0-9A-Za-z ,'.&;_\-]+$',
                    }]
            
            
            class taxId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 9
                    min_length = 1
                    regex=[{
                        'pattern': r'^\d{9}$',
                    }]
            
            
            class website(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 48
                    min_length = 1
            
            
            class mcc(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 9999
                    inclusive_minimum = 1
        
            @staticmethod
            def ownershipType() -> typing.Type['OwnershipTypeEnum']:
                return OwnershipTypeEnum
            __annotations__ = {
                "address": address,
                "phone": phone,
                "establishedDate": establishedDate,
                "legalName": legalName,
                "dbaName": dbaName,
                "taxId": taxId,
                "website": website,
                "mcc": mcc,
                "ownershipType": ownershipType,
            }
    
    legalName: MetaOapg.properties.legalName
    ownershipType: 'OwnershipTypeEnum'
    website: MetaOapg.properties.website
    address: 'AddressModel'
    establishedDate: MetaOapg.properties.establishedDate
    phone: MetaOapg.properties.phone
    taxId: MetaOapg.properties.taxId
    dbaName: MetaOapg.properties.dbaName
    mcc: MetaOapg.properties.mcc
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'AddressModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["establishedDate"]) -> MetaOapg.properties.establishedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalName"]) -> MetaOapg.properties.legalName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dbaName"]) -> MetaOapg.properties.dbaName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxId"]) -> MetaOapg.properties.taxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mcc"]) -> MetaOapg.properties.mcc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownershipType"]) -> 'OwnershipTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address", "phone", "establishedDate", "legalName", "dbaName", "taxId", "website", "mcc", "ownershipType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> 'AddressModel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["establishedDate"]) -> MetaOapg.properties.establishedDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalName"]) -> MetaOapg.properties.legalName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dbaName"]) -> MetaOapg.properties.dbaName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxId"]) -> MetaOapg.properties.taxId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mcc"]) -> MetaOapg.properties.mcc: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownershipType"]) -> 'OwnershipTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address", "phone", "establishedDate", "legalName", "dbaName", "taxId", "website", "mcc", "ownershipType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        legalName: typing.Union[MetaOapg.properties.legalName, str, ],
        ownershipType: 'OwnershipTypeEnum',
        website: typing.Union[MetaOapg.properties.website, str, ],
        address: 'AddressModel',
        establishedDate: typing.Union[MetaOapg.properties.establishedDate, str, date, ],
        phone: typing.Union[MetaOapg.properties.phone, str, ],
        taxId: typing.Union[MetaOapg.properties.taxId, str, ],
        dbaName: typing.Union[MetaOapg.properties.dbaName, str, ],
        mcc: typing.Union[MetaOapg.properties.mcc, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BusinessDetailsModel':
        return super().__new__(
            cls,
            *args,
            legalName=legalName,
            ownershipType=ownershipType,
            website=website,
            address=address,
            establishedDate=establishedDate,
            phone=phone,
            taxId=taxId,
            dbaName=dbaName,
            mcc=mcc,
            _configuration=_configuration,
            **kwargs,
        )

from payfactory_python_sdk.model.address_model import AddressModel
from payfactory_python_sdk.model.ownership_type_enum import OwnershipTypeEnum
