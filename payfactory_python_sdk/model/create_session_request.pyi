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


class CreateSessionRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "redirectUrl",
            "refreshUrl",
            "companyName",
            "externalId",
            "completeUrl",
            "signer",
        }
        
        class properties:
        
            @staticmethod
            def signer() -> typing.Type['CreateSessionRequestSignerModel']:
                return CreateSessionRequestSignerModel
            
            
            class companyName(
                schemas.StrSchema
            ):
                pass
            
            
            class redirectUrl(
                schemas.StrSchema
            ):
                pass
            
            
            class completeUrl(
                schemas.StrSchema
            ):
                pass
            
            
            class refreshUrl(
                schemas.StrSchema
            ):
                pass
            
            
            class externalId(
                schemas.StrSchema
            ):
                pass
            
            
            class pricingPlanId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pricingPlanId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def businessDetails() -> typing.Type['SessionBusinessDetailsModel']:
                return SessionBusinessDetailsModel
            __annotations__ = {
                "signer": signer,
                "companyName": companyName,
                "redirectUrl": redirectUrl,
                "completeUrl": completeUrl,
                "refreshUrl": refreshUrl,
                "externalId": externalId,
                "pricingPlanId": pricingPlanId,
                "businessDetails": businessDetails,
            }
    
    redirectUrl: MetaOapg.properties.redirectUrl
    refreshUrl: MetaOapg.properties.refreshUrl
    companyName: MetaOapg.properties.companyName
    externalId: MetaOapg.properties.externalId
    completeUrl: MetaOapg.properties.completeUrl
    signer: 'CreateSessionRequestSignerModel'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signer"]) -> 'CreateSessionRequestSignerModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyName"]) -> MetaOapg.properties.companyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirectUrl"]) -> MetaOapg.properties.redirectUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completeUrl"]) -> MetaOapg.properties.completeUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refreshUrl"]) -> MetaOapg.properties.refreshUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["externalId"]) -> MetaOapg.properties.externalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pricingPlanId"]) -> MetaOapg.properties.pricingPlanId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["businessDetails"]) -> 'SessionBusinessDetailsModel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["signer", "companyName", "redirectUrl", "completeUrl", "refreshUrl", "externalId", "pricingPlanId", "businessDetails", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signer"]) -> 'CreateSessionRequestSignerModel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyName"]) -> MetaOapg.properties.companyName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirectUrl"]) -> MetaOapg.properties.redirectUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completeUrl"]) -> MetaOapg.properties.completeUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refreshUrl"]) -> MetaOapg.properties.refreshUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["externalId"]) -> MetaOapg.properties.externalId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pricingPlanId"]) -> typing.Union[MetaOapg.properties.pricingPlanId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["businessDetails"]) -> typing.Union['SessionBusinessDetailsModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["signer", "companyName", "redirectUrl", "completeUrl", "refreshUrl", "externalId", "pricingPlanId", "businessDetails", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        redirectUrl: typing.Union[MetaOapg.properties.redirectUrl, str, ],
        refreshUrl: typing.Union[MetaOapg.properties.refreshUrl, str, ],
        companyName: typing.Union[MetaOapg.properties.companyName, str, ],
        externalId: typing.Union[MetaOapg.properties.externalId, str, ],
        completeUrl: typing.Union[MetaOapg.properties.completeUrl, str, ],
        signer: 'CreateSessionRequestSignerModel',
        pricingPlanId: typing.Union[MetaOapg.properties.pricingPlanId, None, str, schemas.Unset] = schemas.unset,
        businessDetails: typing.Union['SessionBusinessDetailsModel', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateSessionRequest':
        return super().__new__(
            cls,
            *args,
            redirectUrl=redirectUrl,
            refreshUrl=refreshUrl,
            companyName=companyName,
            externalId=externalId,
            completeUrl=completeUrl,
            signer=signer,
            pricingPlanId=pricingPlanId,
            businessDetails=businessDetails,
            _configuration=_configuration,
            **kwargs,
        )

from payfactory_python_sdk.model.create_session_request_signer_model import CreateSessionRequestSignerModel
from payfactory_python_sdk.model.session_business_details_model import SessionBusinessDetailsModel
