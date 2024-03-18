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


class ApplicationDetailsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class appId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'appId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class externalId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'externalId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class legalName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'legalName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class dbaName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dbaName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ownershipType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ownershipType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class taxId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'taxId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def address() -> typing.Type['AddressModel']:
                return AddressModel
            
            
            class phone(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phone':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class website(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'website':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def customerService() -> typing.Type['ApplicationDetailsResponseCustomerServiceModel']:
                return ApplicationDetailsResponseCustomerServiceModel
        
            @staticmethod
            def signer() -> typing.Type['ApplicationDetailsResponseSignerModel']:
                return ApplicationDetailsResponseSignerModel
            monthlyTransactionVolume = schemas.Int32Schema
            
            
            class merchantCategoryCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'merchantCategoryCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "appId": appId,
                "externalId": externalId,
                "legalName": legalName,
                "dbaName": dbaName,
                "ownershipType": ownershipType,
                "taxId": taxId,
                "address": address,
                "phone": phone,
                "website": website,
                "customerService": customerService,
                "signer": signer,
                "monthlyTransactionVolume": monthlyTransactionVolume,
                "merchantCategoryCode": merchantCategoryCode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appId"]) -> MetaOapg.properties.appId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["externalId"]) -> MetaOapg.properties.externalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalName"]) -> MetaOapg.properties.legalName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dbaName"]) -> MetaOapg.properties.dbaName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownershipType"]) -> MetaOapg.properties.ownershipType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxId"]) -> MetaOapg.properties.taxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'AddressModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerService"]) -> 'ApplicationDetailsResponseCustomerServiceModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signer"]) -> 'ApplicationDetailsResponseSignerModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyTransactionVolume"]) -> MetaOapg.properties.monthlyTransactionVolume: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantCategoryCode"]) -> MetaOapg.properties.merchantCategoryCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["appId", "externalId", "legalName", "dbaName", "ownershipType", "taxId", "address", "phone", "website", "customerService", "signer", "monthlyTransactionVolume", "merchantCategoryCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appId"]) -> typing.Union[MetaOapg.properties.appId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["externalId"]) -> typing.Union[MetaOapg.properties.externalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalName"]) -> typing.Union[MetaOapg.properties.legalName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dbaName"]) -> typing.Union[MetaOapg.properties.dbaName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownershipType"]) -> typing.Union[MetaOapg.properties.ownershipType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxId"]) -> typing.Union[MetaOapg.properties.taxId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['AddressModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerService"]) -> typing.Union['ApplicationDetailsResponseCustomerServiceModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signer"]) -> typing.Union['ApplicationDetailsResponseSignerModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyTransactionVolume"]) -> typing.Union[MetaOapg.properties.monthlyTransactionVolume, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantCategoryCode"]) -> typing.Union[MetaOapg.properties.merchantCategoryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["appId", "externalId", "legalName", "dbaName", "ownershipType", "taxId", "address", "phone", "website", "customerService", "signer", "monthlyTransactionVolume", "merchantCategoryCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        appId: typing.Union[MetaOapg.properties.appId, None, str, schemas.Unset] = schemas.unset,
        externalId: typing.Union[MetaOapg.properties.externalId, None, str, schemas.Unset] = schemas.unset,
        legalName: typing.Union[MetaOapg.properties.legalName, None, str, schemas.Unset] = schemas.unset,
        dbaName: typing.Union[MetaOapg.properties.dbaName, None, str, schemas.Unset] = schemas.unset,
        ownershipType: typing.Union[MetaOapg.properties.ownershipType, None, str, schemas.Unset] = schemas.unset,
        taxId: typing.Union[MetaOapg.properties.taxId, None, str, schemas.Unset] = schemas.unset,
        address: typing.Union['AddressModel', schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, None, str, schemas.Unset] = schemas.unset,
        website: typing.Union[MetaOapg.properties.website, None, str, schemas.Unset] = schemas.unset,
        customerService: typing.Union['ApplicationDetailsResponseCustomerServiceModel', schemas.Unset] = schemas.unset,
        signer: typing.Union['ApplicationDetailsResponseSignerModel', schemas.Unset] = schemas.unset,
        monthlyTransactionVolume: typing.Union[MetaOapg.properties.monthlyTransactionVolume, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        merchantCategoryCode: typing.Union[MetaOapg.properties.merchantCategoryCode, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicationDetailsResponse':
        return super().__new__(
            cls,
            *args,
            appId=appId,
            externalId=externalId,
            legalName=legalName,
            dbaName=dbaName,
            ownershipType=ownershipType,
            taxId=taxId,
            address=address,
            phone=phone,
            website=website,
            customerService=customerService,
            signer=signer,
            monthlyTransactionVolume=monthlyTransactionVolume,
            merchantCategoryCode=merchantCategoryCode,
            _configuration=_configuration,
            **kwargs,
        )

from payfactory_python_sdk.model.address_model import AddressModel
from payfactory_python_sdk.model.application_details_response_customer_service_model import ApplicationDetailsResponseCustomerServiceModel
from payfactory_python_sdk.model.application_details_response_signer_model import ApplicationDetailsResponseSignerModel