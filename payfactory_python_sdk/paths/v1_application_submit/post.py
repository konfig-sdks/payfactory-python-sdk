# coding: utf-8

"""
    Payfactory Api

    Payfactory specializes in embedded payment facilitation (payfac) services for ISVs and SaaS companies. Our gateway-friendly platform integrates with software systems to provide seamless payment facilitation with little to no development required, allowing our partners to minimize integration costs and quickly gain a new revenue stream. Founded by payment industry veterans, we believe that integrated processing should be simple, frictionless and fast – while also maintaining the highest level of security, customer service and human support.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from payfactory_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from payfactory_python_sdk.api_response import AsyncGeneratorResponse
from payfactory_python_sdk import api_client, exceptions
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

from payfactory_python_sdk.model.pricing_model import PricingModel as PricingModelSchema
from payfactory_python_sdk.model.processing_details_model import ProcessingDetailsModel as ProcessingDetailsModelSchema
from payfactory_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema
from payfactory_python_sdk.model.owner_model import OwnerModel as OwnerModelSchema
from payfactory_python_sdk.model.business_details_model import BusinessDetailsModel as BusinessDetailsModelSchema
from payfactory_python_sdk.model.risk_contact_model import RiskContactModel as RiskContactModelSchema
from payfactory_python_sdk.model.person_model import PersonModel as PersonModelSchema
from payfactory_python_sdk.model.customer_service_contact_model import CustomerServiceContactModel as CustomerServiceContactModelSchema
from payfactory_python_sdk.model.bank_details_model import BankDetailsModel as BankDetailsModelSchema
from payfactory_python_sdk.model.application_submit_request_model import ApplicationSubmitRequestModel as ApplicationSubmitRequestModelSchema
from payfactory_python_sdk.model.application_submit_response_model import ApplicationSubmitResponseModel as ApplicationSubmitResponseModelSchema

from payfactory_python_sdk.type.processing_details_model import ProcessingDetailsModel
from payfactory_python_sdk.type.application_submit_request_model import ApplicationSubmitRequestModel
from payfactory_python_sdk.type.pricing_model import PricingModel
from payfactory_python_sdk.type.risk_contact_model import RiskContactModel
from payfactory_python_sdk.type.error_response import ErrorResponse
from payfactory_python_sdk.type.owner_model import OwnerModel
from payfactory_python_sdk.type.person_model import PersonModel
from payfactory_python_sdk.type.business_details_model import BusinessDetailsModel
from payfactory_python_sdk.type.customer_service_contact_model import CustomerServiceContactModel
from payfactory_python_sdk.type.bank_details_model import BankDetailsModel
from payfactory_python_sdk.type.application_submit_response_model import ApplicationSubmitResponseModel

from ...api_client import Dictionary
from payfactory_python_sdk.pydantic.risk_contact_model import RiskContactModel as RiskContactModelPydantic
from payfactory_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from payfactory_python_sdk.pydantic.application_submit_response_model import ApplicationSubmitResponseModel as ApplicationSubmitResponseModelPydantic
from payfactory_python_sdk.pydantic.pricing_model import PricingModel as PricingModelPydantic
from payfactory_python_sdk.pydantic.business_details_model import BusinessDetailsModel as BusinessDetailsModelPydantic
from payfactory_python_sdk.pydantic.bank_details_model import BankDetailsModel as BankDetailsModelPydantic
from payfactory_python_sdk.pydantic.owner_model import OwnerModel as OwnerModelPydantic
from payfactory_python_sdk.pydantic.application_submit_request_model import ApplicationSubmitRequestModel as ApplicationSubmitRequestModelPydantic
from payfactory_python_sdk.pydantic.person_model import PersonModel as PersonModelPydantic
from payfactory_python_sdk.pydantic.customer_service_contact_model import CustomerServiceContactModel as CustomerServiceContactModelPydantic
from payfactory_python_sdk.pydantic.processing_details_model import ProcessingDetailsModel as ProcessingDetailsModelPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = ApplicationSubmitRequestModelSchema


request_body_application_submit_request_model = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'ApiKey',
]
SchemaFor200ResponseBodyApplicationJson = ApplicationSubmitResponseModelSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ApplicationSubmitResponseModel


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ApplicationSubmitResponseModel


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_application_mapped_args(
        self,
        isv_name: str,
        business_details: BusinessDetailsModel,
        customer_service_contact: CustomerServiceContactModel,
        risk_contact: RiskContactModel,
        business_contact: PersonModel,
        processing_details: ProcessingDetailsModel,
        bank_details: BankDetailsModel,
        pricing_structure: PricingModel,
        external_id: typing.Optional[typing.Optional[str]] = None,
        owners: typing.Optional[typing.Optional[typing.List[OwnerModel]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if external_id is not None:
            _body["externalId"] = external_id
        if isv_name is not None:
            _body["isvName"] = isv_name
        if business_details is not None:
            _body["businessDetails"] = business_details
        if customer_service_contact is not None:
            _body["customerServiceContact"] = customer_service_contact
        if risk_contact is not None:
            _body["riskContact"] = risk_contact
        if business_contact is not None:
            _body["businessContact"] = business_contact
        if processing_details is not None:
            _body["processingDetails"] = processing_details
        if bank_details is not None:
            _body["bankDetails"] = bank_details
        if pricing_structure is not None:
            _body["pricingStructure"] = pricing_structure
        if owners is not None:
            _body["owners"] = owners
        args.body = _body
        return args

    async def _acreate_new_application_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Submit a new Application
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/Application/Submit',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_application_submit_request_model.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_new_application_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Submit a new Application
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/Application/Submit',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_application_submit_request_model.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateNewApplicationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_application(
        self,
        isv_name: str,
        business_details: BusinessDetailsModel,
        customer_service_contact: CustomerServiceContactModel,
        risk_contact: RiskContactModel,
        business_contact: PersonModel,
        processing_details: ProcessingDetailsModel,
        bank_details: BankDetailsModel,
        pricing_structure: PricingModel,
        external_id: typing.Optional[typing.Optional[str]] = None,
        owners: typing.Optional[typing.Optional[typing.List[OwnerModel]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_application_mapped_args(
            isv_name=isv_name,
            business_details=business_details,
            customer_service_contact=customer_service_contact,
            risk_contact=risk_contact,
            business_contact=business_contact,
            processing_details=processing_details,
            bank_details=bank_details,
            pricing_structure=pricing_structure,
            external_id=external_id,
            owners=owners,
        )
        return await self._acreate_new_application_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_application(
        self,
        isv_name: str,
        business_details: BusinessDetailsModel,
        customer_service_contact: CustomerServiceContactModel,
        risk_contact: RiskContactModel,
        business_contact: PersonModel,
        processing_details: ProcessingDetailsModel,
        bank_details: BankDetailsModel,
        pricing_structure: PricingModel,
        external_id: typing.Optional[typing.Optional[str]] = None,
        owners: typing.Optional[typing.Optional[typing.List[OwnerModel]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_application_mapped_args(
            isv_name=isv_name,
            business_details=business_details,
            customer_service_contact=customer_service_contact,
            risk_contact=risk_contact,
            business_contact=business_contact,
            processing_details=processing_details,
            bank_details=bank_details,
            pricing_structure=pricing_structure,
            external_id=external_id,
            owners=owners,
        )
        return self._create_new_application_oapg(
            body=args.body,
        )

class CreateNewApplication(BaseApi):

    async def acreate_new_application(
        self,
        isv_name: str,
        business_details: BusinessDetailsModel,
        customer_service_contact: CustomerServiceContactModel,
        risk_contact: RiskContactModel,
        business_contact: PersonModel,
        processing_details: ProcessingDetailsModel,
        bank_details: BankDetailsModel,
        pricing_structure: PricingModel,
        external_id: typing.Optional[typing.Optional[str]] = None,
        owners: typing.Optional[typing.Optional[typing.List[OwnerModel]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> ApplicationSubmitResponseModelPydantic:
        raw_response = await self.raw.acreate_new_application(
            isv_name=isv_name,
            business_details=business_details,
            customer_service_contact=customer_service_contact,
            risk_contact=risk_contact,
            business_contact=business_contact,
            processing_details=processing_details,
            bank_details=bank_details,
            pricing_structure=pricing_structure,
            external_id=external_id,
            owners=owners,
            **kwargs,
        )
        if validate:
            return ApplicationSubmitResponseModelPydantic(**raw_response.body)
        return api_client.construct_model_instance(ApplicationSubmitResponseModelPydantic, raw_response.body)
    
    
    def create_new_application(
        self,
        isv_name: str,
        business_details: BusinessDetailsModel,
        customer_service_contact: CustomerServiceContactModel,
        risk_contact: RiskContactModel,
        business_contact: PersonModel,
        processing_details: ProcessingDetailsModel,
        bank_details: BankDetailsModel,
        pricing_structure: PricingModel,
        external_id: typing.Optional[typing.Optional[str]] = None,
        owners: typing.Optional[typing.Optional[typing.List[OwnerModel]]] = None,
        validate: bool = False,
    ) -> ApplicationSubmitResponseModelPydantic:
        raw_response = self.raw.create_new_application(
            isv_name=isv_name,
            business_details=business_details,
            customer_service_contact=customer_service_contact,
            risk_contact=risk_contact,
            business_contact=business_contact,
            processing_details=processing_details,
            bank_details=bank_details,
            pricing_structure=pricing_structure,
            external_id=external_id,
            owners=owners,
        )
        if validate:
            return ApplicationSubmitResponseModelPydantic(**raw_response.body)
        return api_client.construct_model_instance(ApplicationSubmitResponseModelPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        isv_name: str,
        business_details: BusinessDetailsModel,
        customer_service_contact: CustomerServiceContactModel,
        risk_contact: RiskContactModel,
        business_contact: PersonModel,
        processing_details: ProcessingDetailsModel,
        bank_details: BankDetailsModel,
        pricing_structure: PricingModel,
        external_id: typing.Optional[typing.Optional[str]] = None,
        owners: typing.Optional[typing.Optional[typing.List[OwnerModel]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_application_mapped_args(
            isv_name=isv_name,
            business_details=business_details,
            customer_service_contact=customer_service_contact,
            risk_contact=risk_contact,
            business_contact=business_contact,
            processing_details=processing_details,
            bank_details=bank_details,
            pricing_structure=pricing_structure,
            external_id=external_id,
            owners=owners,
        )
        return await self._acreate_new_application_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        isv_name: str,
        business_details: BusinessDetailsModel,
        customer_service_contact: CustomerServiceContactModel,
        risk_contact: RiskContactModel,
        business_contact: PersonModel,
        processing_details: ProcessingDetailsModel,
        bank_details: BankDetailsModel,
        pricing_structure: PricingModel,
        external_id: typing.Optional[typing.Optional[str]] = None,
        owners: typing.Optional[typing.Optional[typing.List[OwnerModel]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_application_mapped_args(
            isv_name=isv_name,
            business_details=business_details,
            customer_service_contact=customer_service_contact,
            risk_contact=risk_contact,
            business_contact=business_contact,
            processing_details=processing_details,
            bank_details=bank_details,
            pricing_structure=pricing_structure,
            external_id=external_id,
            owners=owners,
        )
        return self._create_new_application_oapg(
            body=args.body,
        )

